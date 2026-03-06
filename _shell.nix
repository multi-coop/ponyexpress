{ pkgs ? import <nixpkgs> {} }:

with pkgs;

mkShell {
buildInputs = [
    python315 poetry # python tools
    go-task # alternative to make
    typst # to generate pdf
    nodejs_24 #for the doc
];

shellHook = ''
        export GRIST_API_KEY="API KEY disponible via votre compte GRIST"
    '';

}
