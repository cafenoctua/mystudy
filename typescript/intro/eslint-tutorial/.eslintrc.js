module.exports = {
    root: true,
    env: {
      browser: true,
      es2021: true,
    },
    parserOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
    },
    rules: {
      "no-console": "error",
      camelcase: ["error", { properties: "never" }],
    },
  };