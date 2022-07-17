"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.DefaultTemplate = void 0;
var tslib_1 = require("tslib");
var fs_extra_1 = tslib_1.__importDefault(require("fs-extra"));
var inversify_1 = require("inversify");
var DefaultTemplate = /** @class */ (function () {
    function DefaultTemplate() {
    }
    DefaultTemplate.prototype.generateFile = function (nameOfFileWithExtension, fileContent, hasPath, pathOfFile) {
        if (hasPath === void 0) { hasPath = false; }
        if (pathOfFile === void 0) { pathOfFile = ''; }
        this.createFile(pathOfFile, nameOfFileWithExtension, fileContent);
    };
    ;
    DefaultTemplate.prototype.createFile = function (pathOfFile, fileName, fileContent) {
        var filepath = process.cwd() + "".concat(pathOfFile, "/").concat(fileName);
        fs_extra_1.default.writeFile(filepath, fileContent, function (error) {
            if (!error) {
                console.log("File created: ".concat(fileName));
            }
            else {
                console.error("File error: ".concat(fileName));
            }
        });
    };
    DefaultTemplate = tslib_1.__decorate([
        (0, inversify_1.injectable)()
    ], DefaultTemplate);
    return DefaultTemplate;
}());
exports.DefaultTemplate = DefaultTemplate;
