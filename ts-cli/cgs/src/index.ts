import 'reflect-metadata';
import { Container } from 'inversify';
import { CLI } from './cli';
import { FeatureRequest } from './templates/github/feature-request.template';
import { DefaultTemplate } from './templates/default/default.template';
import { MergeRequest } from './templates/gitlab/merge-request.template';

export function index(): CLI {
  const container: Container = new Container();

  // Default Template
  container.bind<DefaultTemplate>('DefaultTemplate').to(DefaultTemplate).inSingletonScope();

  // Github Template
  container.bind<FeatureRequest>('FeatureRequest').to(FeatureRequest).inSingletonScope();

  // Gitlab Template
  container.bind<MergeRequest>('MergeRequest').to(MergeRequest).inSingletonScope();

  container.bind<CLI>('CLI').to(CLI).inSingletonScope();

  return container.get<CLI>('CLI');
}

index();