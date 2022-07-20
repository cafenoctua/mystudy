"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.index = void 0;
require("reflect-metadata");
var inversify_1 = require("inversify");
var cli_1 = require("./cli");
var feature_request_template_1 = require("./templates/github/feature-request.template");
var default_template_1 = require("./templates/default/default.template");
var merge_request_template_1 = require("./templates/gitlab/merge-request.template");
function index() {
    var container = new inversify_1.Container();
    // Default Template
    container.bind('DefaultTemplate').to(default_template_1.DefaultTemplate).inSingletonScope();
    // Github Template
    container.bind('FeatureRequest').to(feature_request_template_1.FeatureRequest).inSingletonScope();
    // Gitlab Template
    container.bind('MergeRequest').to(merge_request_template_1.MergeRequest).inSingletonScope();
    container.bind('CLI').to(cli_1.CLI).inSingletonScope();
    return container.get('CLI');
}
exports.index = index;
index();
