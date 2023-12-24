include .env

.PHONY: dbt_deps
dbt_deps:
	cd ga4_modeling ; \
	dbt deps

.PHONY: dbt_codegen
dbt_codegen:
	cd ga4_modeling ; \
	dbt run-operation generate_source --args '{"schema_name": "${SOURCE_DATABASE}", "database_name": "${SOURCE_PROJECT}"}' > $(output_file)