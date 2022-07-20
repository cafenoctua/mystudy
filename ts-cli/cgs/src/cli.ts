import { injectable, inject } from "inversify";
import { FeatureRequest } from "./templates/github/feature-request.template";
import { GithubChoiceValue, GitlabChoiceValue, Answer, ProviderValue } from "./models/answer-choice";
import { MergeRequest } from "./templates/gitlab/merge-request.template";
import { providerQuestion, githubFileQuestion, gitlabFileQuestion } from "./questions";

@injectable()
export class CLI {
  constructor(@inject('FeatureRequest') private featureReqeust: FeatureRequest,
              @inject('MergeRequest') private mergeRequest: MergeRequest) {
                this.executeCLI();
              }

  public async executeCLI(): Promise<any> {
    let providerAnswer: Answer = await providerQuestion();

    if (providerAnswer.provider === ProviderValue.GITHUB) {
      return this.githubActions();
    } else if (providerAnswer.provider === ProviderValue.GITLAB) {
      return this.gitlabActions();
    }
  }

  private async githubActions() {
    let githubAnswer: Answer = await githubFileQuestion();

    switch (githubAnswer.files) {
      case GithubChoiceValue.FEATURR_REQUERST: {
        return this.featureReqeust.generateFile();
      }
    }
  }

  private async gitlabActions() {
    let gitlabAnswer: Answer = await gitlabFileQuestion();

    switch (gitlabAnswer.files) {
      case GitlabChoiceValue.MERGE_REQUEST: {
        return this.featureReqeust.generateFile();
      }
    }
  }
}