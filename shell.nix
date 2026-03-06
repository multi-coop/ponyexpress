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
        # dinum grist
        export GRIST_API_KEY="4f02dce79a1cb397c40f594152df07b4ca28a000"

        # get grist
        #export GRIST_API_KEY="f817efbc9f263973632398c23b6193a5a0e911ea"

    '';

}
