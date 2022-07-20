"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.githubFileQuestion = void 0;
var tslib_1 = require("tslib");
var inquirer_1 = tslib_1.__importDefault(require("inquirer"));
var answer_choice_1 = require("../models/answer-choice");
function githubFileQuestion() {
    return tslib_1.__awaiter(this, void 0, void 0, function () {
        var listOfFiles;
        return tslib_1.__generator(this, function (_a) {
            listOfFiles = [
                { name: 'Feature request (issue)',
                    value: answer_choice_1.GithubChoiceValue.FEATURR_REQUERST },
            ];
            return [2 /*return*/, inquirer_1.default.prompt([{
                        name: 'files',
                        type: 'list',
                        message: 'Which Github files do you want to generate?',
                        choices: listOfFiles
                    }])];
        });
    });
}
exports.githubFileQuestion = githubFileQuestion;
