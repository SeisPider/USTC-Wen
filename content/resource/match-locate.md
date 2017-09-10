---
title: Match&Locate Download
date: 2015-02-07
aliases:
    - /2015/0207/c10090a113774/page.htm
---

**Update: 2015 February 8**

The Match&Locate package is developed for detecting and locating small earthquakes. The Match&Locate method employs some template events and detects small events through stacking cross-correlograms between waveforms of the template events and potential small event signals in the continuous waveforms over multiple stations and components, but the stacking is performed after making relative traveltime corrections based on the relative locations of the template event and potential small event scanning through a 3-D region around the template. Compared to the current methods of small event detection, the M&L method places event detection to a lower magnitude level and extends the capability of detecting small events that have large distance separations from the template. The method has little dependence on the accuracy of the velocity models used, and, at the same time, provides high-precision location information of the detected small-magnitude events.

***Thanks for using our code. Before downloading, please [click here](http://222.195.83.195/wen/codes/matchlocate/) to fill the form and submit your download request. Requests that are missing information will be rejected.***

**References:**

- Zhang, M. and Wen, L., An effective method for small event detection: Match and Locate (M&L), ***Geophys. J. Int.***, 200 (3): 1523-1537. doi: [10.1093/gji/ggu466](http://dx.doi.org/10.1093/gji/ggu466), 2015.
- Zhang, M. and Wen, L., Seismological Evidence for a Low‐Yield Nuclear Test on 12 May 2010 in North Korea, ***Seismol. Res. Lett.***, 86(1), doi: [10.1785/02201401170](http://dx.doi.org/10.1785/02201401170), 2015.


　　微震检测在天然地震和勘探地震领域均有广泛的应用。传统的地震检测方法主要是通过震相识别和到时拾取来实现。但是，由于微震信号极其微弱（甚至噪音量级），传统方法面临失败。近十年来，在地震学中广泛应用着两种均不依赖震相识别和到时拾取的微震检测方法：震源扫描叠加（Source-Scanning Algorithm）和波形匹配技术（Matched filter）。 震源扫描叠加方法通过波形能量叠加来实现地震检测和定位，但是它检测不到极小地震；另外，震源扫描叠加方法依赖精确的速度模型来计算绝对走时。而波形匹配技术则通过互相关波形叠加来实现极小地震的检测。但是，它只能检测那些紧邻参考模板的地震并且不能给出地震的位置信息。
　　温联星研究组结合这两种方法的优势，提出了一种新的微震检测方法：Match and Locate。首先，我们利用参考模板震相与每一个台站记录到的连续波形做滑动互相关。然后，网格化参考模板附近区域，计算每个格点与参考模板位置之间的相对走时；各台站相关波形根据每个格点对应的相对走时和参考震相走时矫正到发震时刻进行叠加。如果叠加后的相关系数和相关信噪比满足设置的阈值，那么我们就在此时刻检测到一个地震，对应的格点即是其位置。应用此新方法，我们能检测到更小震级的地震，而且地震位置有着很高的分辨率。
　　
***如果您想下载使用这个程序，请[点击此处](http://222.195.83.195/wen/codes/matchlocate/)跳转到下载申请页面。您需要在下载申请页面中填写您的个人信息与研究方向，并提交下载申请。程序将通过电子邮件的形式发送给您。***

**参考文献：**

- Zhang, M. and Wen, L., An effective method for small event detection: Match and Locate (M&L), ***Geophys. J. Int.***, 200 (3): 1523-1537. doi: [10.1093/gji/ggu466](http://dx.doi.org/10.1093/gji/ggu466), 2015.
- Zhang, M. and Wen, L., Seismological Evidence for a Low‐Yield Nuclear Test on 12 May 2010 in North Korea, ***Seismol. Res. Lett.***, 86(1), doi: [10.1785/02201401170](http://dx.doi.org/10.1785/02201401170), 2015.
