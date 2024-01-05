include .env

.PHONY: dbt_deps
dbt_deps:
	cd ga4_modeling ; \
	dbt deps

.PHONY: dbt_codegen
dbt_codegen:
	cd ga4_modeling ; \
	dbt run-operation generate_source --args '{"schema_name": "${SOURCE_DATABASE}", "database_name": "${SOURCE_PROJECT}"}' > $(output_file)

.PHONY: dbt_run_force
dbt_run_force:
	cd ga4_modeling ; \
	dbt run -fs staging --vars '{gcp_project: ${GCP_PROJECT}, date: ${DATE}}' ; \
	dbt snapshot --vars '{gcp_project: ${GCP_PROJECT}, date: ${DATE}}' ; \
	dbt run -fs dimensions+ fct_scd__access --vars '{gcp_project: ${GCP_PROJECT}, date: ${DATE}}'

.PHONY: dbt_build
dbt_build:
	cd ga4_modeling ; \
	dbt build --vars '{gcp_project: ${GCP_PROJECT}, date: ${DATE}}'

.PHONY: backfill_fct_access
backfill_fct_access:
	cd ga4_modeling ; \
	dbt run -s +fct__access --vars '{gcp_project: ${GCP_PROJECT}, backfill: true}'