var config = module.exports;

config["App tests"] = {
    rootPath: "../",
    environment: "browser", // or "node"
    sources: [
    ],
    tests: [
        "test/specs/**/*.js",
        "test/specs/*.js"
    ]
}
