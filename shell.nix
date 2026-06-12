with import <nixpkgs> { config.allowUnfree = true; };
mkShell {
  buildInputs = [
    clang
    cmake
    cudatoolkit
    loccount
    pkg-config
    pre-commit
    (python3.withPackages (p: with p; [
      ipython
      numpy
      pip
      pydot
      python-lsp-server
    ]))
    ruff
    uv
  ];
  LD_LIBRARY_PATH = lib.makeLibraryPath [
    (lib.getLib pkgs.stdenv.cc.cc)  # required for numpy
    (lib.getLib pkgs.llvm)          # libLLVM.so
  ];
  CUDA_PATH = "${linuxPackages.nvidia_x11}/lib/libcuda.so";
  OPENCL_PATH = "${ocl-icd}/lib/libOpenCL.so";
  NVRTC_PATH = "${cudatoolkit}/lib/libnvrtc.so";
  shellHook = ''
    export CC="clang"
    uv venv --allow-existing && source .venv/bin/activate
  '';
}
