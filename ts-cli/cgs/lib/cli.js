"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CLI = void 0;
var tslib_1 = require("tslib");
var inversify_1 = require("inversify");
var answer_choice_1 = require("./models/answer-choice");
var questions_1 = require("./questions");
var CLI = /** @class */ (function () {
    function CLI(featureReqeust, mergeRequest) {
        this.featureReqeust = featureReqeust;
        this.mergeRequest = mergeRequest;
        this.executeCLI();
    }
    CLI.prototype.executeCLI = function () {
        return tslib_1.__awaiter(this, void 0, void 0, function () {
            var providerAnswer;
            return tslib_1.__generator(this, function (_a) {
                switch (_a.label) {
                    case 0: return [4 /*yield*/, (0, questions_1.providerQuestion)()];
                    case 1:
                        providerAnswer = _a.sent();
                        if (providerAnswer.provider === answer_choice_1.ProviderValue.GITHUB) {
                            return [2 /*return*/, this.githubActions()];
                        }
                        else if (providerAnswer.provider === answer_choice_1.ProviderValue.GITLAB) {
                            return [2 /*return*/, this.gitlabActions()];
                        }
                        return [2 /*return*/];
                }
            });
        });
    };
    CLI.prototype.githubActions = function () {
        return tslib_1.__awaiter(this, void 0, void 0, function () {
            var githubAnswer;
            return tslib_1.__generator(this, function (_a) {
                switch (_a.label) {
                    case 0: return [4 /*yield*/, (0, questions_1.githubFileQuestion)()];
                    case 1:
                        githubAnswer = _a.sent();
                        switch (githubAnswer.files) {
                            case answer_choice_1.GithubChoiceValue.FEATURR_REQUERST: {
                                return [2 /*return*/, this.featureReqeust.generateFile()];
                            }
                        }
                        return [2 /*return*/];
                }
            });
        });
    };
    CLI.prototype.gitlabActions = function () {
        return tslib_1.__awaiter(this, void 0, void 0, function () {
            var gitlabAnswer;
            return tslib_1.__generator(this, function (_a) {
                switch (_a.label) {
                    case 0: return [4 /*yield*/, (0, questions_1.gitlabFileQuestion)()];
                    case 1:
                        gitlabAnswer = _a.sent();
                        switch (gitlabAnswer.files) {
                            case answer_choice_1.GitlabChoiceValue.MERGE_REQUEST: {
                                return [2 /*return*/, this.featureReqeust.generateFile()];
                            }
                        }
                        return [2 /*return*/];
                }
            });
        });
    };
    CLI = tslib_1.__decorate([
        (0, inversify_1.injectable)(),
        tslib_1.__param(0, (0, inversify_1.inject)('FeatureRequest')),
        tslib_1.__param(1, (0, inversify_1.inject)('MergeRequest'))
    ], CLI);
    return CLI;
}());
exports.CLI = CLI;
