with import <nixpkgs> { config.allowUnfree = true; };
mkShell {
  buildInputs = [
    clang
    cmake
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
  LD_LIBRARY_PATH = lib.makeLibraryPath [
    (lib.getLib pkgs.stdenv.cc.cc)  # required for numpy
    (lib.getLib pkgs.llvm)          # libLLVM.so
    ocl-icd                         # libOpenCL.so
    linuxPackages.nvidia_x11        # libcuda.so
    cudaPackages.cudatoolkit        # libnvrtc.so
  ];
  shellHook = ''
    mkdir -p tmp
    export TMPDIR="$(pwd)/tmp"
    export CC="clang"
  '';
}
