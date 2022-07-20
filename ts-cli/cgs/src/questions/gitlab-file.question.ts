import inquirer from "inquirer";

import { Answer, GitlabChoiceValue, Choice } from "../models/answer-choice";

export async function gitlabFileQuestion(): Promise<Answer> {
  const listOfFiles: Choice[] = [
    {name: 'Merge request',
     value: GitlabChoiceValue.MERGE_REQUEST},
  ];

  return inquirer.prompt([{
    name: 'files',
    type: 'list',
    message: 'Which Gitlab files do you want to generate?',
    choices: listOfFiles
  }]);
}