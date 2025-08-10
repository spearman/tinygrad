with import <nixpkgs> {};
mkShell {
  buildInputs = [
    clang
    cmake
    llvm
    ocl-icd
    pipenv
    pkg-config
    pre-commit
    (python3.withPackages (p: with p; [
      ipython
      pip
      pydot
      python-lsp-server
    ]))
    ruff
    sloccount
  ];
  shellHook = ''
    mkdir -p tmp
    export TMPDIR="$(pwd)/tmp"
    export LD_LIBRARY_PATH="${lib.getLib pkgs.stdenv.cc.cc}/lib:\
      ${pkgs.zlib}/lib:${lib.getLib pkgs.llvm}/lib:${pkgs.ocl-icd}/lib:\
      $LD_LIBRARY_PATH"
    export CC="clang"
  '';
}
