"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.MergeRequest = void 0;
var tslib_1 = require("tslib");
var inversify_1 = require("inversify");
var path_1 = require("../../models/path");
var filename_1 = require("../../models/filename");
var MergeRequest = /** @class */ (function () {
    function MergeRequest(defaultTemplate) {
        this.defaultTemplate = defaultTemplate;
        this.fileName = filename_1.FileName.MERGE_REQUEST;
        this.hasPath = true;
        this.pathOfFile = path_1.GitlabPath.MERGE_REQUEST_TEMPLATE;
    }
    MergeRequest.prototype.generateFile = function () {
        this.defaultTemplate.generateFile(this.fileName, this.fileContent(), this.hasPath, this.pathOfFile);
    };
    MergeRequest.prototype.fileContent = function () {
        return "# What does this implement/fix? Explain your changes.\n\u2026\n## Does this close any currently open issues?\n\u2026\n## Any relevant logs, error output, etc?\n(Please put this in a code block, so it is more readable for reviewers )\n## Any other comments?\n...\n## Where has this been tested?\n**Browsers:**\n- [ ] Chrome\n- [ ] Firefox\n- [ ] Safari\n- [ ] IE 11\n- [ ] Edge\n- [ ] Opera\n        ";
    };
    MergeRequest = tslib_1.__decorate([
        (0, inversify_1.injectable)(),
        tslib_1.__param(0, (0, inversify_1.inject)('DefaultTemplate'))
    ], MergeRequest);
    return MergeRequest;
}());
exports.MergeRequest = MergeRequest;
