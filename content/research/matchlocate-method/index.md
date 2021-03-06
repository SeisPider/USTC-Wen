---
title: 本研究组发展了一种新的微震检测方法
date: 2014-11-20
aliases:
    - /2014/1120/c10094a113654/page.htm
---

微震检测在天然地震和勘探地震领域均有广泛的应用。传统的地震检测方法主要是通过震相识别和到时拾取来实现。但是，由于微震信号极其微弱（甚至噪音量级），传统方法面临失败。近十年来，在地震学中广泛应用着两种均不依赖震相识别和到时拾取的微震检测方法：震源扫描叠加（Source-Scanning Algorithm）和波形匹配技术（Matched filter）。 震源扫描叠加方法通过波形能量叠加来实现地震检测和定位，但是它检测不到极小地震；另外，震源扫描叠加方法依赖精确的速度模型来计算绝对走时。而波形匹配技术则通过互相关波形叠加来实现极小地震的检测。但是，它只能检测那些紧邻参考模板的地震并且不能给出地震的位置信息。

中国科学技术大学地震与地球内部物理实验室博士生张淼和导师温联星教授结合这两种方法的优势，提出了一种新的微震检测方法：Match and Locate （M&L）。首先，我们利用参考模板震相与每一个台站记录到的连续波形做滑动互相关。然后，网格化参考模板附近区域，计算每个格点与参考模板位置之间的相对走时；各台站相关波形根据每个格点对应的相对走时和参考震相走时矫正到发震时刻进行叠加。如果叠加后的相关系数和相关信噪比满足设置的阈值，那么我们就在此时刻检测到一个地震，对应的格点即是其位置。应用此新方法，我们能检测到更小震级的地震，而且地震位置有着很高的分辨率。

**参考文献：**

Zhang, M. and Wen, L., An effective method for small event detection: Match and Locate (M&L), Geophys. J. Int., 200 (3): 1523-1537. doi: 10.1093/gji/ggu466, 2015. [(Full Article Link)](https://academic.oup.com/gji/article/200/3/1523/628438/An-effective-method-for-small-event-detection)

{{<figure src="Fig1.png" caption="图一： (a)示例原始波形，(b)背景噪音信号，(c-i)原始波形降低振幅（乘以左侧数字）加上背景噪音来模拟小震级地震（对应震级从3.2到-0.65），分别用波形匹配技术和M&L方法对其进行检测。灰色虚线代表相关系数阈值。">}}
