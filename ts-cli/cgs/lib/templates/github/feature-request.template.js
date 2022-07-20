"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.FeatureRequest = void 0;
var tslib_1 = require("tslib");
var inversify_1 = require("inversify");
var path_1 = require("../../models/path");
var filename_1 = require("../../models/filename");
var FeatureRequest = /** @class */ (function () {
    function FeatureRequest(defaultTemplate) {
        this.defaultTemplate = defaultTemplate;
        this.fileName = filename_1.FileName.FEATURE_REQUEST;
        this.hasPath = true;
        this.pathOfFile = path_1.GithubPath.ISSU_TEMPLATE;
    }
    FeatureRequest.prototype.generateFile = function () {
        this.defaultTemplate.generateFile(this.fileName, this.fileContent(), this.hasPath, this.pathOfFile);
    };
    FeatureRequest.prototype.fileContent = function () {
        return "---\nname: Feature request\nabout: Suggest an idea for this project\ntitle: ''\nlabels: ''\nassignees: ''\n---\n**Is your feature request related to a problem? Please describe.**\nA clear and concise description of what the problem is. Ex. I'm always frustrated when [...]\n**Describe the solution you'd like**\nA clear and concise description of what you want to happen.\n**Describe alternatives you've considered**\nA clear and concise description of any alternative solutions or features you've considered.\n**Additional context**\nAdd any other context or screenshots about the feature request here.\n        ";
    };
    FeatureRequest = tslib_1.__decorate([
        (0, inversify_1.injectable)(),
        tslib_1.__param(0, (0, inversify_1.inject)('DefaultTemplate'))
    ], FeatureRequest);
    return FeatureRequest;
}());
exports.FeatureRequest = FeatureRequest;
