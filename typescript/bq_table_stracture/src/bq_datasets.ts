import { BigQuery } from "@google-cloud/bigquery";


const bigquery = new BigQuery();

async function listDatasets() {
  const [datasets] = await bigquery.getDatasets();
  let datasetIds = new Array();
  datasets.forEach(
    dataset => {
      datasetIds.push(dataset.id);
    }
  );

  return datasetIds
}

async function listTables(dataset: string) {
  const [tables] = await bigquery.dataset(dataset).getTables();
  let tableIds = Array();
  tables.forEach(
    table => {
      tableIds.push(table.id);
    }
  )

  return tableIds
}

async function main() {
  
  const datasetIds = await listDatasets();
  console.log(datasetIds);

  let datasets_tables: {[id: string]: any; } = {};
  await Promise.all(
    datasetIds.map(
      async(datasetId) => {
        let tableIds = await listTables(datasetId);
        datasets_tables[datasetId] = tableIds;
      }
    )
  )
  
  console.log(datasets_tables);
}

main();