"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.providerQuestion = void 0;
var tslib_1 = require("tslib");
var inquirer_1 = tslib_1.__importDefault(require("inquirer"));
var answer_choice_1 = require("../models/answer-choice");
function providerQuestion() {
    return tslib_1.__awaiter(this, void 0, void 0, function () {
        var listOfFiles;
        return tslib_1.__generator(this, function (_a) {
            listOfFiles = [
                { name: 'Github', value: answer_choice_1.ProviderValue.GITHUB },
                { name: 'Gitlab', value: answer_choice_1.ProviderValue.GITLAB },
            ];
            return [2 /*return*/, inquirer_1.default.prompt([{
                        name: 'provider',
                        type: 'list',
                        message: 'Select a Git hosting provider:',
                        choices: listOfFiles
                    }])];
        });
    });
}
exports.providerQuestion = providerQuestion;
