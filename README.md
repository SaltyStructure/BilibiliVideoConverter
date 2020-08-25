这是一个把Bilibili手机客户端缓存的m4s格式自动合并为mp4的脚本

------------

## 缓存并从手机中导出视频

- 在手机客户端中下载视频
- 打开`文件管理器`，访问`Android - data - tv.danmaku.bili - download`，即可看到名为缓存视频编号的文件夹，将其导出至电脑

## 使用脚本

- 在`Github - Releases`中下载压缩文件并解压，运行`BilibiliVideoConverter.exe`或`BilibiliVideoConverter.py`(如有Python3)
- 在`缓存主目录`中填入电脑中的缓存文件夹位置，如`C:\Users\Public\[视频编号]`。请注意，为防止出现反转义符问题，最好将所有`\`手动替换为`/`
- 在`集数`中输入缓存的最大集数
- 然后脚本会自动合并视频(mp4)与音频(aac)m4s文件至单个mp4，并将其保存至`[脚本目录 - output]`

## 已知的问题

- 反转义符`\`可能会导致字符串识别出错
- 程序是单线程，硬件利用率低
