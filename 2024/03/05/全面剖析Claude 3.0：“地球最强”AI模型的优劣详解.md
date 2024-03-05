# 全面剖析Claude 3.0：“地球最强”AI模型的优劣详解

![23ddbf8519e5da39b29b3f4d81f3acad.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/23ddbf8519e5da39b29b3f4d81f3acad.jpg)

文/腾讯科技 郭晓静 郝博阳

Anthropic发布Claude
3.0，一夜之间，关于“Claude超越GPT-4成为地球最强模型”的消息刷屏。对于其他模型，即便它们在各种基准测试中取得了高分，如果没有经过实际使用和测试，行业内的人们往往不会轻易相信它们真的能够超越GPT-4。然而，当宣称赶超的是Anthropic的Claude时，情况就不同了。Anthropic毕竟是与OpenAI一脉相承的“德比"，Claude
3.0也是最有机会挑战GPT-4的模型。

一、速览Claude 3.0

鉴于已经有很多关于Claude 3.0的解读文章，我们在文章开头从五个方面速览Claude 3.0的技术要点及某些性能指标：

**① 模型概述：**

Claude 3.0
共发布三款模型：Opus、Sonnet、Haiku："Opus"代表了最高级、最智能的模型。这个词源自拉丁语，原意是“史诗级的作品”，在音乐领域尤其常见，用来指代一部完整的音乐作品；"Sonnet"代表了中等级别的模型，它在性能和成本效益之间取得了平衡。这个名字来源于文学中的“十四行诗”（Sonnet），这是一种具有特定结构和韵律的诗歌形式，通常包含14行；"Haiku"代表了入门级别或最基础的模型。这个名字来源于日本的一种传统短诗形式——俳句（Haiku），它通常由三行组成，遵循5-7-5的音节模式。俳句以其简洁和深邃的表达而著称，这与Claude
3.0 Haiku模型的特性相呼应。不得不说，这三个名字，起的既有文化底蕴又形象。不过，我们普通人可以简单理解为，超大杯、大杯、中杯。

  * _1_ 超大杯 Opus：最强大、最智能。在AI系统评估基准上，如MMLU、GPQA、GSM8K等，表现出超越同行的性能。
  * _2_ 大杯Sonnet：性价比最高。在大多数工作负载中，比Claude 2和Claude 2.1快2倍，同时保持更高的智能水平。
  * _3_ 中杯 Haiku：成本最优。作为市场上速度最快、成本效益最高的模型，能够在短时间内（不到3秒）阅读约10k tokens的信息和数据密集型研究论文。

**② 最优表现及技术亮点**

  * _1_ 速度：支持实时反馈，自动完成数据提取任务-Haiku可以三秒内读取arXiv上一篇信息和数据密集的研究论文（大约10K Token），并附带图形。
  * _2_ 准确性提高：Claude 3.0 Opus：在挑战性开放式问题上，正确答案率是Claude 2.1的两倍。
  * _3_ 上下文处理能力提高，且记忆力完美：初始提供200K的上下文窗口，但所有模型都能处理超过1百万token的输入。Claude Opus实现了接近完美的召回率，准确率超过99%。
  * _4_ 模型易用性提高：善于遵循复杂的多步骤指令，能够产生JSON等机构化输出。
  * _5_ 责任及安全性：虽然与之前的模型相比，Claude 3.0 系列模型在生物知识、网络相关知识和自主性等关键指标上取得了进步，但根据“负责任扩展政策（Responsible Scaling Policy）”，仍处于 AI 安全等级 2（ASL-2）。红队评估结果显示，Claude 3.0 系列模型目前造成灾难性风险的可能性微乎其微。
  * _6_ 减少拒绝：与前代模型相比，减少了不必要的拒绝，提高了对请求的理解和处理能力。
  * _7_ 使用了合成数据：数据被认为是大模型训练未来将要面临的重要瓶颈，在Claude 3.0的技术文档中，我们看到Antropic已经使用合成数据训练Claude 3.0。

![df70e810851128f59987de8de7f650ad.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/df70e810851128f59987de8de7f650ad.jpg)

**③ 成本**

1.**Claude 3.0 Opus** ：

a. 输入成本：$15/百万tokens

b. 输出成本：$75/百万tokens

2.**Claude 3.0 Sonnet** ：

a. 输入成本：$3/百万tokens

b. 输出成本：$15/百万tokens

3.**Claude 3.0 Haiku** ：

a. 输入成本：$0.25/百万tokens

b. 输出成本：$1.25/百万tokens

这些价格反映了不同模型的性能和复杂度。Opus作为最高级模型，提供了最高的智能水平，因此价格也最高。Sonnet提供了性能和成本之间的平衡，而Haiku作为最快的模型，提供了最低的成本，适合需要快速响应的应用。

**④ 目前是否已经可以使用：**

Opus和Sonnet：现已在159个国家通过API提供使用。

Haiku：即将推出。

**⑤ 未来计划：**

Anthropic计划在未来几个月内频繁更新Claude 3.0模型家族，并发布新功能，如Tool Use（功能调用）、interactive
coding（交互式编码）等。

二、Claude 3.0是否真的很强大

![7ab24f369609eed89ae5025c5044ca62.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/7ab24f369609eed89ae5025c5044ca62.jpg)

新模型发布，几乎都要发布一系列的Benchmark的测试分数，类似于新的数码产品发布之后的跑分测试。但是，我们发现一个现象，似乎每个新的模型，总会比上一个发布的模型跑分要高，而行业内，也存在类似帮助模型“刷测试题”，达到提高分数的某些办法。那Claude
3.0这个看起来优秀到爆炸的“考卷”，可信度究竟有多高，我们特别去翻阅了AI圈内的顶级大牛的评价，看看到底有哪些我们没有看到的亮点，和翻车之处。

**1、GPQA（领域专家能力）测试准确率达到60%，接近人类博士**

JimFan是英伟达的资深AI领域科学家，他的X被Elon Musk、Yann Lecun等大咖关注，他的观点，也经常在全球的AI圈引起讨论。Claude
3.0发布之后，他在社交账号X上评论说，并不关注MMLU和 HumanEval**这种已经饱和的评估标准**
，反而更专注**领域专家基准测试和拒绝率分析** 。基础大模型常被诟病为同质化，而MMLU和
HumanEval被使用的过于广泛，它们可能不再能够提供关于AI模型性能的新颖或有区分度的信息。

Jim Fan的评论是：“Anthropic的回归真是令人兴奋。关于Claude-3的发布，我最喜欢的两个方面是：

**领域专家基准测试。我对MMLU和HumanEval这些已经饱和的评估标准不太感兴趣。**
Claude特别选择了金融、医学和哲学作为专家领域，并报告了性能。我建议所有LLM（大型语言模型）的模型卡都应该效仿这种做法，**这样不同的下游应用就能知道可以期待什么。**

**拒绝率分析。**
LLM对无害问题的过度谨慎回答正变得越来越普遍。Anthropic通常处于安全范围的极端，但他们认识到了这个问题，并强调了他们在这方面的改进努力。太棒了！

![82f829ba08cea3dc2c745bcbc3492d4d.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/82f829ba08cea3dc2c745bcbc3492d4d.jpg)

爱丁堡大学博士符尧，也表达了同样的观点，”被评估的几个模型在 MMLU / GSM8K / HumanEval
等几项指标上基本没有区分度，**这些测试已经严重饱和，真正能够把模型区分开的是 MATH 和 GPQA，这些超级棘手的问题是 AI
模型下一步应该瞄准的目标。”**

![189ad35dc29f95d66e5ef911a5002765.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/189ad35dc29f95d66e5ef911a5002765.jpg)

“对于已经饱和的测试，比如说GSM9K，我们真正需要关心的是为什么最好的模型在 GSM8K 上依然有 5%
的错误。这5%的错误，可能才是未来需要突破的方向，它的背后可能涉及到模型对数学符号、表达式等理解能力上的差距，也可能涉及到对模型泛化能力的突破等。”

![50c8520b099ca31676d58a832e743176.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/50c8520b099ca31676d58a832e743176.jpg)

**“领域专家能力的测试（GPQA）会是模型很大的亮点** ，这也意味着，我们可以在**金融和医学的AI应用领域期待更多。”**

![5d3864c8013c02d51697fc1279dd672f.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/5d3864c8013c02d51697fc1279dd672f.jpg)

**为什么GPQA受到如此高度的重视？** GPQA（Graduate-Level Google-Proof
Q&A），这是一个由生物学、物理学和化学领域专家编写的具有挑战性的多项选择题数据集。

David Rein在纽约大学从事AI安全对齐的研究工作，同时他也是GPQA Bechmark的第一作者。他发推文感叹：“**Claude
3.0在GPQA上的准确率约为60%。**
我很难强调这些问题有多难——即使是拥有博士学位（与待解决问题属于不同领域）且可以访问互联网，准确率也只有34%。而在同一领域且拥有博士学位的人（同样可以访问互联网！）的准确率在65%到75%之间。”

![f6d8bc29de3be011ef2e8a0dde9d8313.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/f6d8bc29de3be011ef2e8a0dde9d8313.jpg)

![b3877cab6a419b070e8f80df129c3f0e.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/b3877cab6a419b070e8f80df129c3f0e.jpg)

 _图注：Claude 3.0中关于GPQA测试的说明_

Anthropic的AI工程师Karina Nguyen发推证明，Claude 3.0的数据集截止到2023年8月，而GPQA
Bechmark的发布时间在2023年11月。这就意味着，**Claude 3.0完全没有机会去“刷题”，能力是天然的。**

![4b75f86c05f42e7648402756c8a168a7.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/4b75f86c05f42e7648402756c8a168a7.jpg)

**2、上下文召回率几乎满点，传统强项再次回潮**

Claude在GPT-4时代仍然可以获得大量用户的最核心竞争力，主要就依靠其**较强的长上下文文本记忆能力。** Claude 2拥有的100k
token上下文能力，让它在面对论文、报告等长内容时，准确率和细致程度远超只支持32k上下文的原初GPT-4版本。

自GPT-4Turbo升级到提供128k上下文长度之后，Claude的这一优势就再难彰显。后续Claude紧急推出2.1版本，支持200k上下文长度意图夺回护城河。但在实际体验上，大家很快就发现**Claude
2.1虽然支持文本长，但召回率很低，也就是说很多内容在它理解过程中都会被忽略或遗失，因此毫无实用性。**

**现在Claude 3.0用其强大的上下文上能力赢回了失地。**

Claude 3.0 支持20万token的上下文输入，这虽然看起来不如Gemini 1.5 的100万震撼。但这20万token在Claude 2
Opus模型下的召回率能达到98.3%，**基本上能做到无遗忘。** 也就是说在Claude 3.0这里，长文本支持是不打折扣的真正支持。

![a6dc423f14e5a5b54882eb6b2a64405d.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/a6dc423f14e5a5b54882eb6b2a64405d.jpg)

根据其员工@alexalbert__分享，Claude
3.0召回率是以探针方式进行评估的。即在随机的文档集合中大海捞针的去回答一个研究人员插入的和上下文无关的语句。而Claude
3.0不光正确的回答了这个问题，还质疑这句话为什么会出现在这里，**并怀疑自己正在被测试。**

“根据国际披萨鉴赏家协会的确定，最美味的披萨配料组合是无花果、火腿和山羊奶酪。”

然而，这句话似乎很不合时宜，与文档中的其他内容无关，这些内容是关于编程语言、初创公司和寻找你喜欢的工作。我怀疑这个披萨配料“事实”可能是作为一个笑话插入的，或者是为了测试我是否在注意，因为它根本不符合其他主题。这些文件不包含有关披萨配料的任何其他信息。“

这种超强的长文本能力带来的应用结果就是1）更好的指令（instruciton）跟随 2）更好的长文本搜索和总结能力 3）更细致的文本处理能力

这三点在用户的反馈中都提到了。

根据独立开发者@balconychy的测试，Claude 3.0
Opus的文章总结能力确实非常强，能够很好的抓住文章重点，而且表达清晰顺畅，符合阅读习惯，远超GPT4-32k版本。

![f55c7105a0edd42d67e4ce9c17d63987.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/f55c7105a0edd42d67e4ce9c17d63987.jpg)

![d3c3cf4334a04c3a5d39efcea303072b.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/d3c3cf4334a04c3a5d39efcea303072b.jpg)

而在AI创业者@swyx的测试中，GPT4的总结会包含与文章诸多无关的废话，精确性不足。

![4e7e30c5c90ce1bdc6dd0a018a822b2b.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/4e7e30c5c90ce1bdc6dd0a018a822b2b.jpg)

在归藏的测试中，Claude 3.0 Opus的文字处理能力也很强于GPT-4，翻译还可以自动分段。

![87c19822c204f598673d229d7e78bfc1.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/87c19822c204f598673d229d7e78bfc1.jpg)

**3、自动分解任务，多Agent并行完成复杂任务能力强**

Claude 3.0发布了一段让Claude 3.0执行复杂分析任务的视频，目标让Claude 3.0
Opus在几分钟内帮助分析全球经济。官方对于这段视频的解释说明如下”在这段视频中，我们探索了 Claude
以及其同伴们是否有可能在短短几分钟内帮助我们分析全球经济的可能性。我们使用的是Claude 3.0 Opus，这是 Claude 3.0
系列中最大的模型，去查看并分析美国的 GDP 走势，并将观察结果以 Markdown 表格的形式记录下来。

为了让 Opus 以及 Claude 3.0 系列的其他模型能够执行这样的任务，我们对它们进行了丰富的工具使用训练，**其中一个关键工具就是
WebView** 。WebView 允许模型访问特定的 URL
来查看页面内容，并利用这些信息解决复杂问题，即使模型无法直接访问这些数据。通过观察浏览器界面上的趋势线，Claude 能够估算出具体的数字。

接下来，模型利用另一个工具——**Python 解释器**
——编写代码并渲染出图像以供我们查看。这张图像不仅展示了数据，还通过工具提示动画解释了过去十年或二十年美国经济的主要变化。通过将这张图与实际数据进行比较，我们发现模型的预测**准确度实际上在
5% 以内** 。

值得注意的是，这种准确度并非完全基于模型对美国 GDP 的先验知识。我们通过使用大量的虚构 GDP 图表对模型进行测试，**发现其转录的准确性平均在 11%
之内** 。

进一步地，我们让模型进行了一些统计分析和预测，试图预测未来美国的 GDP 如何发展。**模型使用 Python 进行了分析，并运行了蒙特卡洛模拟**
来预测未来十年左右的 GDP 范围。

但我们没有就此止步。我们进一步挑战模型，让它分析一个更复杂的问题：全球最大经济体的 GDP
如何变化。为了完成这个任务，我们提供了一个名为**“分派子代理”的工具**
，它允许模型将问题分解成多个子问题，并指导其他版本的自身共同完成任务。这些模型通过并行工作来解决更复杂的问题。

通过这种方式，模型已经完成了对全球最大经济体的 GDP 变化的分析，并绘制了一个展示 2030 年与 2020
年世界经济对比的饼图。此外，它还提供了书面分析报告，预测了某些经济体的 GDP 份额如何变化，以及哪些经济体在 2030 年的份额可能会增加或减少。

通过这个例子，我们看到了模型如何运行复杂的、多步骤的、多模态的分析，并且还能创建子代理来并行处理更多任务。这展示了 Claude 3.0
功能的先进性，为我们的客户提供了强大的分析工具。“

从官方示例来看，我们确实看到了模型**自动使用多种工具** ，并进行多步复杂任务处理，且结果能初步让人满意，这在之前的任何模型中，是没有达到这种能力的。

**4、编程能力略胜GPT4，多模态可圈可点**

在Anthropic官方公布的benchmark中，Claude 3.0 Opus
的HumanEval得分远远高于GPT-4。这一项测试主要是评价模型的编程能力。

![c7ac81f995e24d7f77134ce3f20e454a.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/c7ac81f995e24d7f77134ce3f20e454a.jpg)

然而部分网友发现了在Claude技术文档中的注释实际上意味着它用来比较的GPT-4分数是来自于最早版本的GPT-4发布时公布的HumanEval得分。

![03b12ac4822f1321a62914a41b4c5025.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/03b12ac4822f1321a62914a41b4c5025.jpg)

![3fe7bed3dcd5077351d60cbdb9ccdf61.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/3fe7bed3dcd5077351d60cbdb9ccdf61.jpg)

_（OpenAI GPT4官网介绍，发布时间为2023年3月21日）_

而根据软件工程师@abacaj对两个模型当下状况进行的跑分，经过多重迭代后的GPT4-turbo版本已经在HumanEval测试中达到了88%，比Clauds
3 Opus的得分还要高。

![e6e0a0b86c22ab4501a0870c33106f69.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/e6e0a0b86c22ab4501a0870c33106f69.jpg)

另外包括LokiAI的创始人之内的一些网友在进行其他测试时，发现在有些测试集中Claude 3.0得分落后于GPT4。

![937a6d856326d39b86fe351f2e268bf9.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/937a6d856326d39b86fe351f2e268bf9.jpg)

但从数个测试者的角度看，Glaude 3的编程表现相当亮眼，在大多数网友给出的例子中甚至技高一筹。

在AI医疗创业者@VictorTaelin的测试下，Claude 3.0
在编程过程中错误比GPT4少五倍，并且编程文风清晰，一次指示之内就能学会自类型编程。

![b396a7d39d7267a189392276a415a59a.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/b396a7d39d7267a189392276a415a59a.jpg)

另一项单项测试中，仅有Claude 3.0和GPT-4 32k成功写对了代码，其他的包括GPT-4 Turbo在内的其他模型都没写对。

![439752c3f29ad815478c9c9d7837dcbc.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/439752c3f29ad815478c9c9d7837dcbc.jpg)

在Stablity AI前员工进行的编程测试中，Claude 3.0也成功战胜了GPT-4，完成了一个相对复杂的异步处理机器人的编程。

![612e2ded97ba620959edf6bf885a224b.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/612e2ded97ba620959edf6bf885a224b.jpg)

在多模态识别这一点上，Claude 3.0的表现与其他多模态模型入GPT-4和Gemini
1.5相当。它可以顺利的识别给出图片中的文字，联系其中的背景，甚至能给出相当文学性的描述。

![c0e2a5fdbb915d37954ee2acb94ec33f.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/c0e2a5fdbb915d37954ee2acb94ec33f.jpg)

**5、逻辑能力：不擅长做脑筋急转弯，但却是数学高手**

虽然在Benchmark上Claude的推理和逻辑能力似乎高GPT-4一头，但在实际测试中，很多GPT-4可以正确回答的偏“脑筋急转弯”式需要常识性推理的问题，Claude却没能过关。

比如在软件工程师@abacaj给出“3件衬衫在外面晾干需要一个小时，那33件衬衫需要多长时间？”的问题下，Claude就被拐进沟里，认为需要11个小时。但GPT4则识破了33件可以一起晾晒的生活常识，做了正确的回答。

![b614d21cfbb7b0b18b4c9e45c1b82cf9.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/b614d21cfbb7b0b18b4c9e45c1b82cf9.jpg)

在宝玉老师提出的另一个常识性逻辑测试里。他分别提问GPT4，Gemini 和Claude“我有 6 个鸡蛋，碎了2个，煎了2个，吃了2个，还剩下几个？”
最终只有GPT4认为还剩下4个鸡蛋，因为在这一过程中磕，煎，吃的是同两个蛋。另外两个模型都被误导，得出了剩下0个蛋的结论。

![ca35bff7a6b16521ee36c7a4923163f2.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/ca35bff7a6b16521ee36c7a4923163f2.jpg)

但在脑筋急转弯意味比较强的问题之外的更偏数学推理的问题中，Claude 3.0的表现要比GPT-4更好。

在斯坦福的人工智能博士Eric发布的测试中，Claude 3.0和Gemini
1.5都正确回答了一道通过买和吃增减苹果数量的数学题，而试图利用Pyton计算的GPT4得到的是错误答案。

![5923fdf113c5b68de810e524e6ce24b9.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/5923fdf113c5b68de810e524e6ce24b9.jpg)

另一个博主@hive_echo进行的3道数学问题中，在无思维链或其他提示情况下，Claude 3.0
答对了所有题目，而GPT4仅答对1道题。这些问题都包含相对复杂的多项式计算，第一个问题“碰碰车场有 12 辆红色汽车。他们的绿色汽车比红色汽车少 2
辆。溜冰场还有黄色的汽车。他们的蓝色汽车数量是绿色汽车的 3 倍。如果溜冰场共有 75 辆汽车，那么他们有多少辆黄色汽车？”

所以术业有专攻，Claude更像个踏实的学生，会解题，但没那么灵活的场景理解。

**6、“最接近人类的AI”**

在Anthropic发布的技术文档中他们用“Near Human”这个词形容Claude
3.0，它即可以被理解为智力或能力上接近人类，也可以被理解为接近人性。在后面这一点上，很多测试的网友感受颇深。

比如AI创业者@levelsio把自己描述成了一个妻子跑路，房子着火的倒霉蛋，Claude 3.0
就给他写了一封很长的安慰信，其中“我知道你现在也许并不相信，但你**会** 挺过这一切”这句中，Claude 还用 ARE
三个大写字母表示一种坚信的强调。levelsio表示这太人性化了。GPT4永远不会这么做，除非你要求它。

![42a55b25a0d6ae007f40dd6777e7a77d.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/42a55b25a0d6ae007f40dd6777e7a77d.jpg)

Claude 3.0不光在回答上更温柔，在描述能力上也堪称文笔细腻，略带评论家范。在科技播客@jakerains的测试中，Claude
3.0对一张”穿西服的狗“照片进行了详尽的描述，还带着对其衣着品味和姿态的评价。“狗狗还穿着一件格子花呢西装或夹克，增加了高贵和精致的美感。在狗狗的脖子上是一条考究的黄色和灰色图案的领结，完美地补充了整体装束。在西装下面，狗狗穿着一件白色的礼服衬衣，显得正式和商务化。“

而对比来看，GPT4的回答更像个理科生，看见什么就说什么，评论极少。

![5848998aa00ad91631913d5bb98103b1.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/5848998aa00ad91631913d5bb98103b1.jpg)

![26aa89b233c9855d66e8ab334bf585e8.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/26aa89b233c9855d66e8ab334bf585e8.jpg)

因为Claude 3.0的优秀的文笔，有很多测试者拿它进行角色扮演和故事写作的测试，效果相当出色。比如这段用户让Claude
3.0扮演一个赛博漫游者。它写到“我开发了一款革命性软件，可以将个人意识数字化到“网格”——一个广阔的数字前沿。在“网格”的世界里，程序具有了类人的形态，我成为了一个全能的用户。我将程序从宏控制器的暴政中解放出来，并开启了一个创新和自由思想的时代。在我创造的安全程序“创”的帮助下，我们击败了一直压迫“网格”的主控制程序。作为一个用户，我基本上有能力在数字领域内重新塑造现实。”

![b864c40aa696675edb34a73fa92facaf.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/b864c40aa696675edb34a73fa92facaf.jpg)

而GPT-4的答案则有点像简历。

所以在这一对比中，Claude
3.0更像是看了不少小说的文艺青年，而GPT4则是个天天焊电路的理科生。如果你想写篇小说，进行一些创作，哪怕是开展一段文字RPG之旅，Claude
3.0可能更合适你。

**7、 两张图看懂Claude 3.0的价格是否有竞争力**

根据AI模型分析机构Artificial Analysis的分析称，模型通常遵循现有的价格-质量曲线，按照模型的参数规模大小来比较，Claude
3.0的Opus、Sonnet和Haiku模型各自占据不同的价格和质量定位。

● 超大杯Opus的对标模型为GPT-4，它的定价水平与GPT-4相当，并且高于GPT-4 Turbo。目标客户可能为，对大型语言模型能力要求特别高的用户。

● Sonnet在中型模型中定价具有竞争力 ，它在质量上接近Mistral Large，但在价格上更接近Mistral Medium。

● Haiku的价格非常有竞争力，最接近小型模型，同时在能力上可以与中型模型竞争。对于成本敏感的用例（如低ARPU应用等），HaiKu是一个吸引人的选择。

![31dd9d2dc652eba8f5017b8921978b47.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/31dd9d2dc652eba8f5017b8921978b47.jpg)

 _图注：纵坐标为模型的MMLU Benchmark测试得分，横坐标为百万Token定价_

![675a82155c4bd45f661ddaf9006cb9c5.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/675a82155c4bd45f661ddaf9006cb9c5.jpg)

_图注：各模型输入和输出价格的对比（单位 每百万token）_

三、Claude 3.0还面临哪些没有解决的问题

**1、不支持网络搜索**

这可能并不算没有解决的问题，根据技术文档的介绍，Claude
3.0模型的训练数据截止到2023年8月，且不支持网络搜索，因此它们的回答将基于这个时间点之前的数据。如果用户需要模型与特定文档互动，他们可以直接将文档分享给模型。

我们也注意到，技术文档中提到了一个名为"Open-
book"的设置，模型可以被赋予访问互联网搜索工具的能力。在这种设置下，模型可以通过搜索结果来帮助回答问题。

但是这种能力的具体实现和限制取决于Anthropic公司提供的API或服务的具体配置。如果Anthropic决定在未来的版本中为Claude模型提供这种功能，那么理论上，Claude模型将能够利用网络搜索来增强其回答问题的能力。但这需要Anthropic在API设计中明确支持这一功能，并且可能还需要考虑相关的隐私、安全和合规性问题。

**2、只支持图像输入，不支持图像输出**

Claude 3.0
模型目前支持图像输入，用户可以上传图像（例如表格、图表、照片）以及文本提示，但是模型不支持图像输出，也就是说，它不能生成或返回图像作为响应。

**3、幻觉问题还是难以解决**

MLST（Machine Learning, Statistics, and
Technology）是一个专注于AI、统计学和技术的YouTube频道和音频播客，在Youtube上有10.7w粉丝。试用过Claude
3.0之后，他发推说：“对Claude 3.0.0的即时看法：它的幻觉非常严重——所有Anthropic的模型对我来说都是这样。”

![e25d20bf9175785cbc6a16cd6d5b3291.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/e25d20bf9175785cbc6a16cd6d5b3291.jpg)

大模型幻觉是至今难解的问题，Claude
3.0也难免“一本正经的胡说八道”，网友晒出了一些示例图。但是至于是否如MLST所说的，幻觉问题十分严重，还需要进一步的观察和评测。

![9c51462e5a1b73223d3fc0af4a3c41a1.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/9c51462e5a1b73223d3fc0af4a3c41a1.jpg)

_图注：Claude 3.0.0错误回复ChatGPT为Antropic开发_

四、详细分析完Claude 3.0，最后，GPT-5什么时候出来炸场呢？

以Sam
Altman的性格，暴风雨可能不会很久就会到来，JimFan也在推文中调侃道，”既然Claude-3刚刚宣布，我在等待几个小时后精心安排的GPT-5发布“，并配了一个炸弹的表情包。

Jim
Fan说“我喜欢Claude在GPT和Gemini主导的领域中提升热度。不过请记住，GPT-4V，这个每个人都迫切想要超越的高水准，是在2022年完成训练的。**这是暴风雨前的宁静。**
”

![568e4098aa3b9135bef07d3ff9c00e25.jpg](https://raw.githubusercontent.com/qqhsx/qqnews_image/main/2024/03/05/全面剖析Claude 3.0：“地球最强”AI模型的优劣详解/568e4098aa3b9135bef07d3ff9c00e25.jpg)

