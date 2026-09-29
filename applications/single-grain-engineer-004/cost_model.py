#!/usr/bin/env python3
"""2026-09-29 us-east-1 budget envelope for Engineer 004.

Observed brief inputs and benchmarked AWS unit rates are separated from assumptions.
This is an engineering envelope, not an AWS quote; rerun the AWS Pricing Calculator
before submission/deployment.
"""
EVENTS_DAY = 50_000_000
DAYS_MONTH = 30
SECONDS_DAY = 86_400
SPIKE_MULT = 10
ASSUMED_EVENT_BYTES = 1024

KINESIS_ODS_INGEST_PER_GB = 0.08
KINESIS_ODS_RETRIEVAL_PER_GB = 0.04
KINESIS_ODS_STREAM_HOUR = 0.04
FLINK_KPU_HOUR = 0.11
FLINK_RUNNING_GB_MONTH = 0.10
FARGATE_VCPU_SECOND = 0.000011244
FARGATE_GB_SECOND = 0.000001235
DDB_WRITE_PER_MILLION = 0.625
DDB_READ_PER_MILLION = 0.125
DDB_STORAGE_GB_MONTH = 0.25

FLINK_KPUS = 8
FARGATE_BASE_TASKS = 8
FARGATE_PEAK_TASKS = 32
FARGATE_PEAK_FRACTION = 0.10
FARGATE_VCPU_PER_TASK = 1
FARGATE_GB_PER_TASK = 2
DDB_WRITES_PER_EVENT = 1
DDB_READS_MILLION_MONTH = 300
DDB_HOT_STORAGE_GB = 500
S3_STEADY_STORAGE_GB = 2250
S3_GB_MONTH_ASSUMED = 0.023
UNMODELED_RESERVE = 15_000
BUDGET_CEILING = 50_000

avg_eps = EVENTS_DAY / SECONDS_DAY
peak_eps = avg_eps * SPIKE_MULT
ingest_gb_month = EVENTS_DAY * DAYS_MONTH * ASSUMED_EVENT_BYTES / 1_000_000_000

kinesis = (ingest_gb_month * (KINESIS_ODS_INGEST_PER_GB + KINESIS_ODS_RETRIEVAL_PER_GB)
           + 24 * DAYS_MONTH * KINESIS_ODS_STREAM_HOUR)
flink = ((FLINK_KPUS + 1) * 24 * DAYS_MONTH * FLINK_KPU_HOUR
         + FLINK_KPUS * 50 * FLINK_RUNNING_GB_MONTH)
per_task_month = ((FARGATE_VCPU_PER_TASK * FARGATE_VCPU_SECOND)
                  + (FARGATE_GB_PER_TASK * FARGATE_GB_SECOND)) * 3600 * 24 * DAYS_MONTH
avg_tasks = FARGATE_BASE_TASKS * (1 - FARGATE_PEAK_FRACTION) + FARGATE_PEAK_TASKS * FARGATE_PEAK_FRACTION
fargate = avg_tasks * per_task_month
writes_million = EVENTS_DAY * DAYS_MONTH * DDB_WRITES_PER_EVENT / 1_000_000
dynamodb = (writes_million * DDB_WRITE_PER_MILLION
            + DDB_READS_MILLION_MONTH * DDB_READ_PER_MILLION
            + DDB_HOT_STORAGE_GB * DDB_STORAGE_GB_MONTH)
s3 = S3_STEADY_STORAGE_GB * S3_GB_MONTH_ASSUMED
modeled_subtotal = kinesis + flink + fargate + dynamodb + s3
budget_envelope = modeled_subtotal + UNMODELED_RESERVE

print(f"[Estimated] avg_events_per_second={avg_eps:.1f}")
print(f"[Estimated] peak_events_per_second={peak_eps:.1f}")
print(f"[Assumed] ingest_gb_per_30d={ingest_gb_month:.1f}")
print(f"[Estimated] kinesis_usd_month={kinesis:.2f}")
print(f"[Estimated] flink_usd_month={flink:.2f}")
print(f"[Estimated] fargate_usd_month={fargate:.2f}")
print(f"[Estimated] dynamodb_usd_month={dynamodb:.2f}")
print(f"[Estimated] s3_storage_usd_month={s3:.2f}")
print(f"[Estimated] modeled_subtotal_usd_month={modeled_subtotal:.2f}")
print(f"[Assumed] unmodeled_reserve_usd_month={UNMODELED_RESERVE:.2f}")
print(f"[Estimated] budget_envelope_usd_month={budget_envelope:.2f}")
print(f"[Estimated] headroom_to_50k_usd_month={BUDGET_CEILING-budget_envelope:.2f}")

for writes_per_event in (1, 2, 3):
    ddb_writes = EVENTS_DAY * DAYS_MONTH * writes_per_event / 1_000_000 * DDB_WRITE_PER_MILLION
    scenario = modeled_subtotal - (writes_million * DDB_WRITE_PER_MILLION) + ddb_writes + UNMODELED_RESERVE
    print(f"[Sensitivity] writes_per_event={writes_per_event} budget_envelope_usd_month={scenario:.2f}")
