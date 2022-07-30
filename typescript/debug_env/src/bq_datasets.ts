import { BigQuery } from "@google-cloud/bigquery";

function main() {
  const bigquery = new BigQuery();

  async function listDatasets() {
    const [datasets] = await bigquery.getDatasets();
    console.log('Datasets');
    datasets.forEach(dataset => console.log(dataset.id));
  }

  listDatasets();
}

main();