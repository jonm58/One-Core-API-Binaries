**欢迎使用One-Core-API二进制文件！**
***
**语言:**    
[English](README.md) | [简体中文](README_CN.md) | [Русский](README_RU.md) | [Українська](README_UK.md) | [日本語](README_JP.md) | [Português do Brasil](README_BR.md)
***

该存储库包含One-Core-API项目的二进制发布版本。这些版本兼容于Windows Server 2003 SP2、Windows XP SP3和Windows XP x64 SP2。

**官方Discord服务器**: https://discord.gg/eRcGuFtn6p  

**警告**
 该软件使用各个系统中的修改文件，包含仍处于测试或实验阶段的其他文件，并且只有一名开发人员。  换句话说，不可能预测所有可能类型的计算机或虚拟机上的所有可能场景。  在XP/2003和Vista之间，新的API、新技术和对现有API的修改都有最大的飞跃，因此NT5很难达到与NT6相同水平的兼容性。  保持冷静，谨慎，在说这个软件不好或“垃圾”之前，请尽快报告问题中的缺陷，我们将对其进行分析，并尝试纠正问题。  帮助我，抱怨或诽谤该软件对任何人都没有任何好处。

**注意**：  
- 可能不支持Windows XP的非官方SP4以及Integral Edition!

**语言支持**：  
几乎所有Windows的语言：葡萄牙语-巴西（我的语言），葡萄牙语（葡萄牙），土耳其语，中文（繁体和简体），法语，意大利语，匈牙利语，乌克兰语（部分支持），西班牙语，波兰语，俄语和韩语；

**此存储库中的文件夹:**  
- Documents（文档）：项目文档、已知错误、sfxcab使用（用于制作安装程序）等。
- Packages\x86 和 Packages\x64：按包分类的二进制发布版本。您可以直接从这里下载和安装/更新这些包（例如，转到Packages\x86\Base installer\update并运行update.exe）。
- Todo（待办事项）：待办任务
- Test（测试）：一些用于测试的二进制文件和文档；
- Release（发布）：生成新二进制版本的脚本；
- Output（输出）：二进制输出，您可以使用发布文件夹中的脚本生成；

**One-Core-API二进制项目由以下包组成：**  
警告：如果OCA包需要重新启动，请执行。如果您安装了所有包并且仅在最后一个包上重新启动，则Windows将损坏。
- **Base（基础）**：One-Core-API的主要包，是所有其他包（除了App Compat和Driver Update）所必需的，其中包含此项目中使用的所有包装（如kernelbase和ntext）；
- **Additional Dlls（额外的DLL）**：引入了Windows后期版本的多个新dll。
- **D3d（D3D）**：D3D运行时（主要是基于WineD3D的DX10和DX11）；
- **App Compat（应用程序兼容性）**：应用程序兼容性设置，从Windows后期版本向后兼容。
- **Driver Update（驱动程序更新）**：带来更新的acpi驱动器，支持ACPI 2.0，新驱动器如Storachi（适用于AHCI驱动器控制器），NVME（适用于NVME M.2驱动器控制器）和USBXHCI（USB 3.0）；
- **Branding（品牌）**：引入了Windows Vista上的新品牌系统，D3D和Modern Setup包都需要此包。

**包的安装顺序：**  
- **常规顺序**：Base-> Additional Dlls -> Branding -> D3d -> Driver Update -> App Compat；
- **仅Base包（不需要其他包一起安装，除非您需要）**
  - **仅App Compat（应用程序兼容性）**：此包可以单独安装；
  - **仅Driver Update（驱动程序更新）**：此包可以单独安装；
  - **AppCompat first（首先安装AppCompat）**：此包可以单独安装。

**主要功能**：  
- 默认情况下，增加对128 GB(x86)和2 TB(x64)内存的支持；
- 允许运行为现代Windows OS设计的新程序；
- 支持具有新驱动程序控制器的新硬件；
- 允许在任何计算机上安装Windows，并且支持通用化硬件；
**Modern Setup - 详细**  
这是一个设计用于准备Windows能够安装到其他计算机的包。如果您不想捕获Windows安装，就不需要安装这个包。
- 安装完One-Core-API Modern Setup并重新启动计算机后，您可以运行Sysprep，一个准备Windows成为通用化安装到任何硬件的工具；
- Sysprep位于：Windows\System32\Sysprep，就像Windows Vista一样；
- 这个工具与Vista上的相似。为了在XP/2003上达到与Vista或更高系统上安装到新计算机相同的行为，您必须运行sysprep.exe并选择"进入系统外箱体验（OOBE）"的操作。推荐同时选择“通用化”。选择操作和标记后，您可以在关闭选项中选择是否仅退出程序，关闭或重新启动系统。按下“确定”后，sysprep将运行清理插件并执行所选的关机选项；
- 关闭系统后，在下次启动时，将运行位于Windows\System32\oobe\setup.exe的setup.exe，并检测硬件，检测硬件后将重新启动并进入msoobe；
- 要修补Windows Vista - Win11设置并捕获Windows XP/2003/Longhorn/Reactos镜像，请使用此工具：https://github.com/Skulltrail192/One-Core-API-Tools

![Sysprep](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/615ada04-a036-43c4-ac54-824cade0b5c2)

**One-Core-API允许您运行：**  
- JetBrains WebStorm 2018；
- JetBrains Intellij 2018（其他版本也可能可用)；
- JetBrains WebStorm 2023.x.x（目前仅适用于Windows XP x64）
- JetBrains IntelliJ 2023.x.x （目前仅适用于Windows XP x64）
- Adobe Photoshop CC 2018;
- Filezilla（最新版本）；
- Visual Studio Code 1.83.1；
- Chrome版本到123以上！；
- Opera版本最高到106；
- Firefox版本最高到122（有一些错误)；
- Microsoft Edge版本最高到122；
- Brave版本1.62.153 (Chromium 121)；
- Yandex最新版本；
- Thorium浏览器版本109以上；
- Supermium版本122以上；
- Seamonkey版本2.53.10以上；
- Thunderbird版本121以上；
- 傲游浏览器版本7.1.6以上；
- Vivaldi最新版本；
- JDK 1.8（目前仅适用于Windows XP x64)；
- Java Alternative JDK或OpenJDK直到版本21（其他版本可能也有效）。您可以从以下网址下载：https://bell-sw.com/pages/downloads/#/java-11-lts；
- Epic Browser 120；
- Python 3.6；
- .Net Framework最高到4.8；
- Geekbench 4.2；
- Performance Test；
- Adobe Reader DC（2018年版）；
- 福昕阅读器 (2023);
- Windows 7游戏；
- Windows 7画图(小畫家)；
- Windows 7写字板；
- Vista原生应用程序；
- Spotify Windows 7和Windows 10版本；
- Zoom；
- 其他应用程序；
- Node 10.24；
- Telegram Desktop;
- Winrar 7.0 Beta 4（最新版本）；
- Directx 9EX、10和11游戏：
  - 极品飞车17：最高通缉(Need for Speed Most Wanted 2012);
  - 极品飞车16：亡命天涯(Need for Speed The Run);
  - 街头霸王5(Street Figther V);
  - 不义联盟：人间之神(njustice: Gods among us);
  - 刺客信条4：黑旗(Assassin's Creed IV Black Flag);
  - 孤岛危机1,2,和3 (directx 10-11模式);
- Kate 23.08.1 (目前仅适用于Windows XP x64)

**已知限制：**  
- 对话框或窗口中的某些地方仅保留英文。  国际化进程正在进行中。  已安装的mui包的一些问题；
 - 新的应用程序安装程序可能无法工作，例如Chrome、Maxthon、Discord、Team Viewer等崩溃且应用程序未安装。  需要使用从其他操作系统复制的预安装版本；
 - Firefox 55-116运行有一些限制；
 - 从 OCA 3.0.5开始，x86 下的应用程序现在可以在 Windows XP/Server 2003 x64 上运行 ~~Firefox 因为版本 54（32 位）无法在Windows XP x64上运行。  Chrome 61+也不行；~~
 - 该软件包无法与 nlite 集成到 Windows Iso，因为使用名为“SFXCAB Substitute”的工具，而不是标准Microsoft版本；
 - 目前不支持从4.6开始的标准.Net Framework安装程序。  您需要一个重新打包的版本，如下所示：https://github.com/abbodi1406/dotNetFx4xW7。  可用如下：https://www.wincert.net/forum/topic/13805-microsoft-net-framework-472-full-x86x64-incl-language-packs-by-ricktendo/#comment-123251。  其他版本也可用，搜索论坛主题；
 - 新版本的palemoon可能面临配置错误问题。
 - Opera 39 - 46 可能需要以下参数才能启动：--disable-gpu（以防止黑屏）和 --single-process（以防止永远加载第一页）；

**报告问题**

**笔记:**

如果您在使用Chrome或基于Chromium的浏览器时遇到问题，请在此链接中报告: https://github.com/Skulltrail192/One-Core-API-Binaries/issues/178.

对于与Firefox或基于Gecko的浏览器相关的问题，请使用以下GitHub链接进行报告: https://github.com/Skulltrail192/One-Core-API-Binaries/issues/214.

如果问题与BSOD（蓝屏死机）相关，请考虑在此页面上报告该问题: https://github.com/Skulltrail192/One-Core-API-Binaries/issues/233.

**问题报告**  
要帮助重现问题，强烈建议**始终**遵循此模板：
- 描述发生的情况。
  例如：尝试加载Windows时总是出现蓝屏。Windows卡在启动屏幕上。Windows总是出现黑屏等；
- 虚拟机/计算机配置
  例如：Vmware 10、VirtualBox 6.1.0或Core 2 Duo 8400、2Gb DDR2、IDE/SATA硬盘；
- Windows版本和配置
  例如：已安装Windows XP Service Pack 3与POSReady 2009更新，并带有此程序列表：Adobe、Office等；
    
（如果需要对特定部分进行翻译或有其他问题，请告诉我！）  

XP/Server 2003:上运行的应用程序的一些屏幕截图
**Chrome 122**
![Chrome 122](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/6442a5b0-036b-48e0-a6e8-3624825d3882)

**Edge 122**
![Edge122](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/734954f4-2540-4657-9a2d-ce6aed809bf5)

**Opera 106**
![Opera106](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/db509ccf-4e66-4e2b-ad4b-fd8512495333)

**Firefox 122**
![Firefox122](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/db647daf-0960-4ace-ad2f-63469dbf3881)

**Basilisk**
![image_2022_04_08T21_38_17_976Z](https://user-images.githubusercontent.com/5159776/178077859-079bfca4-bdb6-402e-8991-b88e7dfe387c.png)

**Vivaldi**
![vivaldi](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/86d5895f-977a-414f-b0d5-0e877a658676)

**Spotify (对于Windows 7)**
![Spotify-Windows7](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/09de7c20-8670-45dc-9471-a6db9349abd0)

**Visual Studio Code 1.81**
![VisualCode](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/b21748b9-25bb-412d-95b3-2219d2efdf42)

**Microsoft Chess 3d**
![Chess3d](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/bd1ad0c6-edde-4ff2-a6e0-074c7379fab6)

**Libre Office 24 (latest)**
![LibreOffice](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/11fd191d-270c-428d-8d41-0498e8fafb3b)
![Writer-LibreOffice](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/e389a39b-febd-45f6-9c6f-25f64e460142)

**Discord 0.309**
![Discord-Login](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/8a4c12b5-19fc-454d-b02a-a1db807d3900)
![Discord](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/eb673541-4e66-4c76-867e-346edbaaa0af)

**Telegram Desktop**
![Telegram-Desktop](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/d23b9add-629d-45a3-a8e1-c331271bc0d3)

**Zoom会议**
![Zoom](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/d002cf1b-c5f4-4c0c-b629-00e031a56765)

**Java 11**
![Capturar](https://user-images.githubusercontent.com/5159776/178078132-da504607-a1ca-4f8d-ae25-6a7eb367bdaa.PNG)

**Avast和Chromium 68**
![Avast](https://user-images.githubusercontent.com/5159776/178078208-c13b3448-ee6a-4c56-9d94-d0c62d51949e.PNG)

**Windows 7桌面便签**
![StickyNotes](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/669ba3e4-b831-4a96-ad40-d87e3e9531e2)

**Windows 7画画(小畫家)**
![画画](https://github.com/Skulltrail192/One-Core-API-Binaries/assets/5159776/81728a44-c9e7-41e8-b68b-8ea7b119ebba)
