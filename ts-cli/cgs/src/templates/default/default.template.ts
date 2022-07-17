import fs from 'fs-extra';

import { injectable } from 'inversify';
import { Answer } from '../../models/answer-choice';

@injectable()
export class DefaultTemplate {

  constructor() {}

  public generateFile(nameOfFileWithExtension: string, fileContent: string, hasPath = false, pathOfFile = ''): void {
    this.createFile(pathOfFile, nameOfFileWithExtension, fileContent);
  };

  private createFile(pathOfFile: string, fileName: string, fileContent: string): void {
    let filepath: string = process.cwd() + `${pathOfFile}/${fileName}`;
    fs.writeFile(filepath, fileContent, (error: Error) => {
      if (!error) {
        console.log(`File created: ${fileName}`);
      } else {
        console.error(`File error: ${fileName}`);
      }
    });
  }
}