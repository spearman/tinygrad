with import <nixpkgs> { config.allowUnfree = true; };
mkShell {
  buildInputs = [
    clang
    cmake
    cudaPackages.cuda_nvcc
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
    loccount
  ];
  LD_LIBRARY_PATH = lib.makeLibraryPath [
    (lib.getLib pkgs.stdenv.cc.cc)  # required for numpy
    (lib.getLib pkgs.llvm)          # libLLVM.so
    #ocl-icd                         # libOpenCL.so
    #linuxPackages.nvidia_x11        # libcuda.so
    cudaPackages.cudatoolkit        # libnvrtc.so
  ];
  CUDA_PATH = "${linuxPackages.nvidia_x11}/lib/libcuda.so";
  OPENCL_PATH = "${ocl-icd}/lib/libOpenCL.so";
  shellHook = ''
    mkdir -p tmp
    export TMPDIR="$(pwd)/tmp"
    export CC="clang"
  '';
}
