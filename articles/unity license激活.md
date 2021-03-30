unity github action 自动构建

# unity license激活

需要在github上进行，此过程不需要secrets变量

```yaml
jobs:
  # This workflow contains a single job called "build"
  activation:
    name: Request manual activation file 🔑
    runs-on: ubuntu-latest
    steps:
    # Request manual activation file
      - name: Request manual activation file
        id: getManualLicenseFile
        uses: game-ci/unity-request-activation-file@v2
        # Upload artifact (Unity_v20XX.X.XXXX.alf)
      - name: Expose as artifact
        uses: actions/upload-artifact@v1
        with:
          name: ${{ steps.getManualLicenseFile.outputs.filePath }}
          path: ${{ steps.getManualLicenseFile.outputs.filePath }}
```

之后点击action -> summary 可以看到artifacts文件列表

![](http://kuroweb.cf/picture/1616804088834.jpg)

把这个文件下载下来，提交到https://license.unity3d.com/manual，然后下载的就是UNITY_LICENSE

之后可以执行自动编译，unity version会自动检测

**在yaml中写入以下代码，前提是secrets中设置好UNITY_LICENSE变量**

```yaml
jobs:
  buildForAllSupportedPlatforms:
    name: Build for ${{ matrix.targetPlatform }}
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        targetPlatform:
          - StandaloneOSX # Build a macOS standalone (Intel 64-bit).
          - StandaloneWindows # Build a Windows standalone.
          - StandaloneWindows64 # Build a Windows 64-bit standalone.
          - StandaloneLinux64 # Build a Linux 64-bit standalone.
          - iOS # Build an iOS player.
          - Android # Build an Android .apk standalone app.
          - WebGL # WebGL.
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0
          lfs: true
      - uses: actions/cache@v2
        with:
          path: Library
          key: Library-${{ matrix.targetPlatform }}
          restore-keys: Library-
      - uses: game-ci/unity-builder@v2
        env:
          UNITY_LICENSE: ${{ secrets.UNITY_LICENSE }}
        with:
          targetPlatform: ${{ matrix.targetPlatform }}
          allowDirtyBuild: true
      - uses: actions/upload-artifact@v2
        with:
          name: Build-${{ matrix.targetPlatform }}
          path: build/${{ matrix.targetPlatform }}
```

