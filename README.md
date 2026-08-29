# **🚀 Awesome Sparse Attention for Visual Generation**

A curated collection of **sparse attention methods for visual generation**,

covering algorithms, systems, and task-level applications.

We organize papers into 4 chapters:

1.. **Training-Free Sparse Attention**

2.. **Trainable and Native Sparse Attention**

3. **Systems and Hardware**

4. **Applications**

The current collection contains **193 papers**, with **117 papers** mapped to concrete visual-generation applications.

Method chapters include visual-generation methods and transferable sparse-attention designs whose mechanisms, systems, or hardware insights inform visual generation.

# **🚀 Quick Start**


- [**1. Training-Free Sparse Attention**](#1-training-free-sparse-attention)

- [**2. Trainable and Native Sparse Attention**](#2-trainable-and-native-sparse-attention)

- [**3. Systems and Hardware**](#3-systems-and-hardware)

- [**4. Applications**](#4-applications)

# **Overview**

Sparse attention accelerates visual generation by selecting a structured subset of query-key interactions and executing attention on that selected support.

The method taxonomy first distinguishes whether sparse behavior is introduced without parameter updates or learned through training. Within each algorithmic branch, static support is determined before the current attention instance, while dynamic support adapts to the current input or runtime state.

The application taxonomy provides an orthogonal task view. A paper can therefore appear in a method section for its sparse-attention mechanism and again in an application section for its task adaptation, practical speedup, and generation-quality behavior.

| Category | Main focus |
|---|---|
| **Training-Free Sparse Attention** | Sparse support introduced directly at inference time without parameter updates |
| **Trainable and Native Sparse Attention** | Sparse support learned during pretraining, finetuning, distillation, or architecture design |
| **Systems and Hardware** | Kernels, compilers, runtimes, distributed execution, and accelerator co-design |
| **Applications** | Image, video, world-model, 3D/4D, and audio-visual generation |


# **1. Training-Free Sparse Attention**

Training-free methods introduce sparse attention directly at inference time while preserving the parameters of the original model.

Their main design axis is the moment at which sparse support becomes available:

- **prior-defined static support** uses an input-independent pattern

- **calibrated or profiled static support** fixes a pattern after offline observation

- **amortized or semi-dynamic support** updates support at selected layers, steps, chunks, or intervals

- **fully online dynamic support** selects support for the current attention instance

## **1.1 Prior-Defined Static Support**

Prior-defined methods use patterns such as local windows, blocks, stripes, dilation, axial layouts, or fixed global tokens. The support can be compiled before runtime and offers predictable execution.

| Year | Paper Links |
|---:|---|
| 2025 | [Generalized Neighborhood Attention: Multi-dimensional Sparse Attention at the Speed of Light](https://arxiv.org/abs/2504.16922) |
| 2025 | [Radial Attention: $O(n\\log n)$ Sparse Attention with Energy Decay for Long Video Generation](https://arxiv.org/abs/2506.19852) |
| 2026 | [LVSA: Training-Free Sparse Attention for Long Video Diffusion](https://arxiv.org/abs/2605.31057) |

## **1.2 Calibrated or Profiled Static Support**

Calibrated methods derive a reusable sparse pattern from profiling data, representative prompts, model statistics, or offline search. The resulting support remains fixed during deployment.

| Year | Paper Links |
|---:|---|
| 2025 | [Compact Attention: Exploiting Structured Spatio-Temporal Sparsity for Fast Video Generation](https://arxiv.org/abs/2508.12969) |
| 2025 | [Fast Video Generation with Sliding Tile Attention](https://arxiv.org/abs/2502.04507) |
| 2025 | [PAROAttention: Pattern-Aware ReOrdering for Efficient Sparse and Quantized Attention in Visual Generation Models](https://arxiv.org/abs/2506.16054) |
| 2025 | [Sparse-vDiT: Unleashing the Power of Sparse Attention to Accelerate Video Diffusion Transformers](https://arxiv.org/abs/2506.03065) |
| 2026 | [Accelerating Text-to-Video Generation with Calibrated Sparse Attention](https://arxiv.org/abs/2603.05503) |
| 2026 | [ScalingAttention: Discovering Intrinsic Sparse Attention Topology for Video Diffusion Transformers](https://arxiv.org/abs/2606.23019) |

## **1.3 Amortized or Semi-Dynamic Support**

Amortized methods refresh sparse support only at selected moments and reuse it across nearby denoising steps, layers, frames, chunks, or requests. They balance adaptivity with selection overhead.

| Year | Paper Links |
|---:|---|
| 2024 | [SampleAttention: Near-Lossless Acceleration of Long Context LLM Inference with Adaptive Structured Sparse Attention](https://arxiv.org/abs/2406.15486) |
| 2025 | [LiteAttention: A Temporal Sparse Attention for Diffusion Transformers](https://arxiv.org/abs/2511.11062) |
| 2025 | [Re-ttention: Ultra Sparse Visual Generation via Attention Statistical Reshape](https://arxiv.org/abs/2505.22918) |
| 2025 | [Sparse VideoGen: Accelerating Video Diffusion Transformers with Spatial-Temporal Sparsity](https://arxiv.org/abs/2502.01776) |
| 2025 | [SparseD: Sparse Attention for Diffusion Language Models](https://arxiv.org/abs/2509.24014) |
| 2026 | [AccelAes: Accelerating Diffusion Transformers for Training-Free Aesthetic-Enhanced Image Generation](https://arxiv.org/abs/2603.12575) |
| 2026 | [HEART: Exploiting Head Heterogeneity in Sparse Attention for Video Diffusion](https://arxiv.org/abs/2605.14513) |
| 2026 | [HyperVAttention: Efficient Sparse Attention with Spatio-Temporal Clustering for Video Diffusion](https://arxiv.org/abs/2607.03012) |
| 2026 | [LoSA: Locality Aware Sparse Attention for Block-Wise Diffusion Language Models](https://arxiv.org/abs/2604.12056) |
| 2026 | [LoSA: Near-Lossless Sparse Attention for Training-Free Video Diffusion Acceleration](https://arxiv.org/abs/2608.12032) |
| 2026 | [Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models](https://arxiv.org/abs/2608.18484) |
| 2026 | [PulseCol: Periodically Refreshed Column-Sparse Attention for Accelerating Diffusion Language Models](https://arxiv.org/abs/2605.20813) |
| 2026 | [RAPID: Reusing Attention Sparsity with Inter-step Adaptation for Efficient Video Diffusion](https://openaccess.thecvf.com/content/CVPR2026/papers/Lin_RAPID_Reusing_Attention_Sparsity_with_Inter-step_Adaptation_for_Efficient_Video_CVPR_2026_paper.pdf) |
| 2026 | [RESA: Bringing Back What Sparse Attention Ignores with Residual Estimation](https://proceedings.iclr.cc/paper_files/paper/2026/file/89bd6217280d1417370c89ee493ba3c7-Paper-Conference.pdf) |
| 2026 | [Token Radius Attention for Efficient Video Generation](https://arxiv.org/abs/2608.02504) |

## **1.4 Fully Online Dynamic Support**

Fully online methods compute sparse support from the current query-key state, feature geometry, similarity estimate, routing score, or runtime budget. They offer fine-grained input adaptivity.

| Year | Paper Links |
|---:|---|
| 2024 | [MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention](https://arxiv.org/abs/2407.02490) |
| 2024 | [Post-Training Sparse Attention with Double Sparsity](https://arxiv.org/abs/2408.07092) |
| 2024 | [Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2406.10774) |
| 2025 | [Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction](https://arxiv.org/abs/2505.11254) |
| 2025 | [DiTVR: Zero-Shot Diffusion Transformer for Video Restoration](https://arxiv.org/abs/2508.07811) |
| 2025 | [DraftAttention: Fast Video Diffusion via Low-Resolution Attention Guidance](https://arxiv.org/abs/2505.14708) |
| 2025 | [FG-Attn: Leveraging Fine-Grained Sparse Attention in Video Diffusion Models](https://arxiv.org/abs/2509.16518) |
| 2025 | [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://arxiv.org/abs/2502.20766) |
| 2025 | [Grouping First, Attending Smartly: Training-Free Acceleration for Diffusion Transformers](https://arxiv.org/abs/2505.14687) |
| 2025 | [Make It Efficient: Dynamic Sparse Attention for Autoregressive Image Generation](https://arxiv.org/abs/2506.18226) |
| 2025 | [PSA: Pyramid Sparse Attention for Efficient Video Understanding and Generation](https://arxiv.org/abs/2512.04025) |
| 2025 | [RainFusion: Adaptive Video Generation Acceleration via Multi-Dimensional Visual Redundancy](https://arxiv.org/abs/2505.21036) |
| 2025 | [RainFusion2.0: Temporal-Spatial Awareness and Hardware-Efficient Block-wise Sparse Attention](https://arxiv.org/abs/2512.24086) |
| 2025 | [Rectified SpaAttn: Revisiting Attention Sparsity for Efficient Video Generation](https://arxiv.org/abs/2511.19835) |
| 2025 | [SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference](https://arxiv.org/abs/2502.18137) |
| 2025 | [Sparse VideoGen2: Accelerate Video Generation with Sparse Attention via Semantic-Aware Permutation](https://arxiv.org/abs/2505.18875) |
| 2025 | [Training-free and Adaptive Sparse Attention for Efficient Long Video Generation](https://arxiv.org/abs/2502.21079) |
| 2025 | [Training-Free Efficient Video Generation via Dynamic Token Carving](https://arxiv.org/abs/2505.16864) |
| 2025 | [Twilight: Adaptive Attention Sparsity with Hierarchical Top-$p$ Pruning](https://arxiv.org/abs/2502.02770) |
| 2025 | [XAttention: Block Sparse Attention with Antidiagonal Scoring](https://arxiv.org/abs/2503.16428) |
| 2026 | [AdaCluster: Adaptive Query-Key Clustering for Sparse Attention in Video Generation](https://arxiv.org/abs/2604.18348) |
| 2026 | [Attention Sparsity is Input-Stable: Training-Free Sparse Attention for Video Generation via Offline Sparsity Profiling and Online QK Co-Clustering](https://arxiv.org/abs/2603.18636) |
| 2026 | [ClusterAttention: A training-free speedup of bidirectional attention](https://arxiv.org/abs/2608.26965) |
| 2026 | [DFSAttn: Dynamic Fine-grained Sparse Attention for Efficient Video Generation](https://arxiv.org/abs/2605.23445) |
| 2026 | [DynamicRad: Content-Adaptive Sparse Attention for Long Video Diffusion](https://arxiv.org/abs/2604.20470) |
| 2026 | [Efficient Audio-Visual Generation via Synchrony-Aware Cross-Modal Sparse Attention](https://arxiv.org/abs/2608.15522) |
| 2026 | [Efficient Long-Context Modeling in Diffusion Language Models via Block Approximate Sparse Attention](https://arxiv.org/abs/2605.19726) |
| 2026 | [Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention](https://arxiv.org/abs/2602.01801) |
| 2026 | [FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation](https://arxiv.org/abs/2607.16190) |
| 2026 | [Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models](https://arxiv.org/abs/2605.31158) |
| 2026 | [Mixture of Distributions Matters: Dynamic Sparse Attention for Efficient Video Diffusion Transformers](https://arxiv.org/abs/2601.11641) |
| 2026 | [PISA: Piecewise Sparse Attention Is Wiser for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.01077) |
| 2026 | [Ride the Wave: Precision-Allocated Sparse Attention for Smooth Video Generation](https://arxiv.org/abs/2604.12219) |
| 2026 | [SCOPE: Subspace Clustering with Online Per-Head Top-K Estimation for Sparse Video Attention](https://arxiv.org/abs/2608.12780) |
| 2026 | [SDiT: Semantic Region-Adaptive for Diffusion Transformers](https://arxiv.org/abs/2601.12283) |
| 2026 | [SimInsert: Seamless Video Object Insertion via Regional Sparse Attention Fusion](https://arxiv.org/abs/2605.23245) |
| 2026 | [Sol-Attn: Accelerating Video Generation Inference via On-the-Fly Attention Sparsification](https://arxiv.org/abs/2607.24027) |
| 2026 | [SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference](https://arxiv.org/abs/2608.03335) |
| 2026 | [SparSTAR: Sparse Attention for SpaceTime AutoRegressive Video Synthesis](https://arxiv.org/abs/2608.10519) |
| 2026 | [SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration](https://arxiv.org/abs/2602.04361) |
| 2026 | [SVG-EAR: Parameter-Free Linear Compensation for Sparse Video Generation via Error-aware Routing](https://arxiv.org/abs/2603.08982) |
| 2026 | [Training-free sparse attention based on cumulative energy filtering](https://arxiv.org/abs/2606.16317) |
| 2026 | [VecAttention: Vector-wise Sparse Attention for Accelerating Long Context Inference](https://arxiv.org/abs/2603.29494) |

# **2. Trainable and Native Sparse Attention**

Trainable and native methods learn sparse behavior through architecture design, pretraining, finetuning, distillation, routing, or optimization objectives.

Their sparse support can remain structurally fixed after training or adapt to the current sample through learned selectors and routing modules.

## **2.1 Prior-Defined Static Support**

These methods train a model around a fixed sparse topology. Common structures include windows, blocks, axial patterns, local-global layouts, and predefined neighborhood graphs.

| Year | Paper Links |
|---:|---|
| 2018 | [Image Transformer](https://arxiv.org/abs/1802.05751) |
| 2019 | [Blockwise Self-Attention for Long Document Understanding](https://arxiv.org/abs/1911.02972) |
| 2019 | [Generating Long Sequences with Sparse Transformers](https://arxiv.org/abs/1904.10509) |
| 2019 | [Your Local GAN: Designing Two Dimensional Local Attention Mechanisms for Generative Models](https://arxiv.org/abs/1911.12287) |
| 2020 | [Big Bird: Transformers for Longer Sequences](https://arxiv.org/abs/2007.14062) |
| 2020 | [ETC: Encoding Long and Structured Inputs in Transformers](https://arxiv.org/abs/2004.08483) |
| 2020 | [Longformer: The Long-Document Transformer](https://arxiv.org/abs/2004.05150) |
| 2020 | [Semantic Layout Manipulation with High-Resolution Sparse Attention](https://arxiv.org/abs/2012.07288) |
| 2021 | [CogView: Mastering Text-to-Image Generation via Transformers](https://arxiv.org/abs/2105.13290) |
| 2021 | [Combiner: Full Attention Transformer with Sparse Computation Cost](https://arxiv.org/abs/2107.05768) |
| 2021 | [GODIVA: Generating Open-DomaIn Videos from nAtural Descriptions](https://arxiv.org/abs/2104.14806) |
| 2021 | [NÜWA: Visual Synthesis Pre-training for Neural visUal World creAtion](https://arxiv.org/abs/2111.12417) |
| 2021 | [VideoGPT: Video Generation using VQ-VAE and Transformers](https://arxiv.org/abs/2104.10157) |
| 2021 | [Zero-Shot Text-to-Image Generation](https://arxiv.org/abs/2102.12092) |
| 2022 | [MM-Diffusion: Learning Multi-Modal Diffusion Models for Joint Audio and Video Generation](https://arxiv.org/abs/2212.09478) |
| 2022 | [NUWA-Infinity: Autoregressive over Autoregressive Generation for Infinite Visual Synthesis](https://arxiv.org/abs/2207.09814) |
| 2022 | [Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation](https://arxiv.org/abs/2212.11565) |
| 2023 | [LongNet: Scaling Transformers to 1,000,000,000 Tokens](https://arxiv.org/abs/2307.02486) |
| 2023 | [Photorealistic Video Generation with Diffusion Models](https://arxiv.org/abs/2312.06662) |
| 2024 | [Open-Sora Plan: Open-Source Large Video Generation Model](https://arxiv.org/abs/2412.00131) |
| 2024 | [Open-Sora: Democratizing Efficient Video Production for All](https://arxiv.org/abs/2412.20404) |
| 2025 | [Articulate That Object Part (ATOP): 3D Part Articulation via Text and Motion Personalization](https://arxiv.org/abs/2502.07278) |
| 2025 | [FPSAttention: Training-Aware FP8 and Sparsity Co-Design for Fast Video Diffusion](https://arxiv.org/abs/2506.04648) |
| 2025 | [GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861) |
| 2025 | [Hilbert-Guided Sparse Local Attention](https://arxiv.org/abs/2511.05832) |
| 2025 | [HilbertA: Hilbert Attention for Image Generation with Diffusion Models](https://arxiv.org/abs/2509.26538) |
| 2025 | [HoloCine: Holistic Generation of Cinematic Multi-Shot Long Video Narratives](https://arxiv.org/abs/2510.20822) |
| 2025 | [MoE-DiffuSeq: Enhancing Long-Document Diffusion Models with Sparse Attention and Mixture of Experts](https://arxiv.org/abs/2512.20604) |
| 2025 | [SA-DiffuSeq: Addressing Computational and Scalability Challenges in Long-Document Generation with Sparse Attention](https://arxiv.org/abs/2512.20724) |
| 2025 | [TalkingMachines: Real-Time Audio-Driven FaceTime-Style Video via Autoregressive Diffusion Models](https://arxiv.org/abs/2506.03099) |
| 2026 | [Avatar V: Scaling Video-Reference Avatar Video Generation](https://arxiv.org/abs/2606.13872) |
| 2026 | [ElasticDiT: Efficient Diffusion Transformers via Elastic Architecture and Sparse Attention for High-Resolution Image Generation on Mobile Devices](https://arxiv.org/abs/2605.15684) |
| 2026 | [Full-4D: Generating Full-Scope 4D Scenes from a Single-View Video](https://arxiv.org/abs/2605.25500) |
| 2026 | [Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players](https://arxiv.org/abs/2605.28816) |
| 2026 | [Hallo-Live: Real-Time Streaming Joint Audio-Video Avatar Generation with Asynchronous Dual-Stream and Human-Centric Preference Distillation](https://arxiv.org/abs/2604.23632) |
| 2026 | [Helix4D: Complex 4D Mesh Generation](https://arxiv.org/abs/2605.26109) |
| 2026 | [Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](https://arxiv.org/abs/2608.23383) |
| 2026 | [MonarchRT: Efficient Attention for Real-Time Video Generation](https://arxiv.org/abs/2602.12271) |
| 2026 | [OSP-Next: Efficient High-Quality Video Generation with Sparse Sequence Parallelism, HiF8 Quantization, and Reinforcement Learning](https://arxiv.org/abs/2605.28691) |
| 2026 | [ReWorld: An Interactive World Model with Long-Horizon Memory](https://arxiv.org/abs/2608.23565) |
| 2026 | [Sculpt4D: Generating 4D Shapes via Sparse-Attention Diffusion Transformers](https://arxiv.org/abs/2604.21592) |
| 2026 | [VMonarch: Efficient Video Diffusion Transformers with Structured Attention](https://arxiv.org/abs/2601.22275) |
| 2026 | [Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](https://arxiv.org/abs/2608.05663) |
| 2026 | [X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling](https://arxiv.org/abs/2605.24892) |

## **2.2 Calibrated or Profiled Static Support**

These methods learn or search a sparse pattern during training or calibration and then deploy the resulting support as a stable execution structure.

| Year | Paper Links |
|---:|---|
| 2019 | [Adaptive Attention Span in Transformers](https://arxiv.org/abs/1905.07799) |
| 2022 | [SwinBERT: End-to-End Transformers with Sparse Attention for Video Captioning](https://arxiv.org/abs/2111.13196) |
| 2025 | [Efficient-vDiT: Efficient Video Diffusion Transformers With Attention Tile](https://arxiv.org/abs/2502.06155) |
| 2025 | [QuantSparse: Comprehensively Compressing Video Diffusion Transformer with Model Quantization and Attention Sparsification](https://arxiv.org/abs/2509.23681) |

## **2.3 Fully Online Dynamic Support**

These methods train selectors, routers, predictors, or sparse-attention modules that choose support for each input, layer, frame, denoising step, or generation state.

| Year | Paper Links |
|---:|---|
| 2020 | [Efficient Content-Based Sparse Attention with Routing Transformers](https://arxiv.org/abs/2003.05997) |
| 2020 | [Reformer: The Efficient Transformer](https://arxiv.org/abs/2001.04451) |
| 2020 | [Sparse Sinkhorn Attention](https://arxiv.org/abs/2002.11296) |
| 2022 | [DynaST: Dynamic Sparse Transformer for Exemplar-Guided Image Generation](https://arxiv.org/abs/2207.06124) |
| 2024 | [SeerAttention: Learning Intrinsic Sparse Attention in Your LLMs](https://arxiv.org/abs/2410.13276) |
| 2024 | [Sparser is Faster and Less is More: Efficient Sparse Attention for Long-Range Transformers](https://arxiv.org/abs/2406.16747) |
| 2025 | [Bidirectional Sparse Attention for Faster Video Diffusion Training](https://arxiv.org/abs/2509.01085) |
| 2025 | [BLADE: Block-Sparse Attention Meets Step Distillation for Efficient Video Generation](https://arxiv.org/abs/2508.10774) |
| 2025 | [BSA: Ball Sparse Attention for Large-scale Geometries](https://arxiv.org/abs/2506.12541) |
| 2025 | [Direct3D-S2: Gigascale 3D Generation Made Easy with Spatial Sparse Attention](https://arxiv.org/abs/2505.17412) |
| 2025 | [DSV: Exploiting Dynamic Sparsity to Accelerate Large-Scale Video DiT Training](https://arxiv.org/abs/2502.07590) |
| 2025 | [Input-Aware Sparse Attention for Real-Time Co-Speech Video Generation](https://arxiv.org/abs/2510.02617) |
| 2025 | [LongCat-Video Technical Report](https://arxiv.org/abs/2510.22200) |
| 2025 | [Mixture of Contexts for Long Video Generation](https://arxiv.org/abs/2508.21058) |
| 2025 | [Mixture of Sparse Attention: Content-Based Learnable Sparse Attention via Expert-Choice Routing](https://arxiv.org/abs/2505.00315) |
| 2025 | [MoBA: Mixture of Block Attention for Long-Context LLMs](https://arxiv.org/abs/2502.13189) |
| 2025 | [MoGA: Mixture-of-Groups Attention for End-to-End Long Video Generation](https://arxiv.org/abs/2510.18692) |
| 2025 | [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://arxiv.org/abs/2502.11089) |
| 2025 | [Optimizing Mixture of Block Attention](https://arxiv.org/abs/2511.11571) |
| 2025 | [SLA: Beyond Sparsity in Diffusion Transformers via Fine-Tunable Sparse-Linear Attention](https://arxiv.org/abs/2509.24006) |
| 2025 | [Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers](https://arxiv.org/abs/2512.16615) |
| 2025 | [USV: Unified Sparsification for Accelerating Video Diffusion Models](https://arxiv.org/abs/2512.05754) |
| 2025 | [VMoBA: Mixture-of-Block Attention for Video Diffusion Models](https://arxiv.org/abs/2506.23858) |
| 2025 | [VORTA: Efficient Video Diffusion via Routing Sparse Attention](https://arxiv.org/abs/2505.18809) |
| 2025 | [VSA: Faster Video Diffusion with Trainable Sparse Attention](https://arxiv.org/abs/2505.13389) |
| 2026 | [AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model](https://arxiv.org/abs/2604.19747) |
| 2026 | [Geometry-Aware Rotary Position Embedding for Consistent Video World Model](https://arxiv.org/abs/2602.07854) |
| 2026 | [Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention](https://arxiv.org/abs/2602.04789) |
| 2026 | [LIVEditor-14B: Lightning Unified Video Editing via In-Context Sparse Attention](https://arxiv.org/abs/2605.04569) |
| 2026 | [LSRM: High-Fidelity Object-Centric Reconstruction via Scaled Context Windows](https://arxiv.org/abs/2604.05182) |
| 2026 | [MotionCraft: Latent World Modeling with Sparse Attention for Visual Upscaling](https://arxiv.org/abs/2608.08553) |
| 2026 | [SALAD: Achieve High-Sparsity Attention via Efficient Linear Attention Tuning for Video Diffusion Transformer](https://arxiv.org/abs/2601.16515) |
| 2026 | [SLA2: Sparse-Linear Attention with Learnable Routing and QAT](https://arxiv.org/abs/2602.12675) |
| 2026 | [SpargeAttention2: Trainable Sparse Attention via Hybrid Top-k+Top-p Masking and Distillation Fine-Tuning](https://arxiv.org/abs/2602.13515) |
| 2026 | [Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/abs/2604.21221) |
| 2026 | [Veda: Scalable Video Diffusion via Distilled Sparse Attention](https://arxiv.org/abs/2605.30325) |
| 2026 | [Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037) |
| 2026 | [Z-Order Transformer for Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2605.13465) |

# **3. Systems and Hardware**

Systems and hardware works turn algorithmic sparsity into measured latency, throughput, memory, communication, and energy improvements.

They mainly differ in:

- sparse data layout and operator implementation

- scheduling and serving policy

- distributed communication strategy

- accelerator architecture and algorithm-hardware co-design

## **3.1 Kernels, Compilers, and Operators**

These works optimize sparse-attention execution through kernels, compiler transformations, tiling, data layouts, load balancing, and fused operators.

| Year | Paper Links |
|---:|---|
| 2022 | [Dynamic N:M Fine-grained Structured Sparse Attention Mechanism](https://arxiv.org/abs/2203.00091) |
| 2024 | [SPLAT: A framework for optimised GPU code-generation for SParse reguLar ATtention](https://arxiv.org/abs/2407.16847) |
| 2025 | [BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding](https://arxiv.org/abs/2512.12087) |
| 2025 | [FlashOmni: A Unified Sparse Attention Engine for Diffusion Transformers](https://arxiv.org/abs/2509.25401) |
| 2025 | [FSA: An Alternative Efficient Implementation of Native Sparse Attention Kernel](https://arxiv.org/abs/2508.18224) |
| 2025 | [Fused3S: Fast Sparse Attention on Tensor Cores](https://arxiv.org/abs/2505.08098) |
| 2026 | [CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention](https://arxiv.org/abs/2607.25291) |
| 2026 | [FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving](https://arxiv.org/abs/2608.19758) |
| 2026 | [IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse](https://arxiv.org/abs/2603.12201) |
| 2026 | [LiteTopK: Exploiting the Curse of Dimensionality for a Fused Indexer-TopK Kernel in Long-Context Sparse Attention](https://arxiv.org/abs/2607.11976) |
| 2026 | [RIS-Kernel: A Model-Agnostic Architecture for Long-Context LLM Inference via Sparse Attention](https://arxiv.org/abs/2607.21927) |

## **3.2 Serving and Runtime Systems**

These works manage sparse-attention execution across requests, batches, memory hierarchies, and changing runtime budgets.

| Year | Paper Links |
|---:|---|
| 2025 | [LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention](https://arxiv.org/abs/2502.14866) |
| 2025 | [NOSA: Native and Offloadable Sparse Attention](https://arxiv.org/abs/2510.13602) |
| 2025 | [Progressive Sparse Attention: Algorithm and System Co-design for Efficient Attention in LLM Serving](https://arxiv.org/abs/2503.00392) |
| 2026 | [Chorus II: Cross-Request Sparsity Reuse for Efficient Image-to-Video Generation](https://arxiv.org/abs/2606.25040) |
| 2026 | [Sol Video Inference Engine: Agent-Native Full-Stack Acceleration Framework for Efficient Video Generation](https://arxiv.org/abs/2606.23743) |
| 2026 | [Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents](https://arxiv.org/abs/2606.06453) |

## **3.3 Distributed and Parallel Execution**

These works coordinate sparse attention across devices through sequence parallelism, sparse communication, partitioning, and distributed scheduling.

| Year | Paper Links |
|---:|---|
| 2025 | [db-SP: Accelerating Sparse Attention for Visual Generative Models with Dual-Balanced Sequence Parallelism](https://arxiv.org/abs/2511.23113) |
| 2025 | [MTraining: Distributed Dynamic Sparse Attention for Efficient Ultra-Long Context Training](https://arxiv.org/abs/2510.18830) |
| 2025 | [SparseServe: Unlocking Parallelism for Dynamic Sparse Attention in Long-Context LLM Serving](https://arxiv.org/abs/2509.24626) |
| 2026 | [DSA: Efficient Inference For Video Generation Models via Distributed Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2026/file/c3728248f3c627d1f16ca5726cdf83f5-Paper-Conference.pdf) |

## **3.4 Accelerators and Co-Design**

These works design hardware dataflows, memory systems, processing elements, and co-designed sparse-attention mechanisms.

| Year | Paper Links |
|---:|---|
| 2020 | [A$^3$: Accelerating Attention Mechanisms in Neural Networks with Approximation](https://arxiv.org/abs/2002.10941) |
| 2021 | [ELSA: Hardware-Software Co-design for Efficient, Lightweight Self-Attention Mechanism in Neural Networks](https://taejunham.github.io/data/elsa_isca21.pdf) |
| 2021 | [Energon: Towards Efficient Acceleration of Transformers Using Dynamic Sparse Attention](https://arxiv.org/abs/2110.09310) |
| 2021 | [Sanger: A Co-Design Framework for Enabling Sparse Attention using Reconfigurable Architecture](https://liqianglu-zju.github.io/files/conference/2021/MICRO_2021_Sanger.pdf) |
| 2021 | [Transformer Acceleration with Dynamic Sparse Attention](https://arxiv.org/abs/2110.11299) |
| 2022 | [A Length Adaptive Algorithm-Hardware Co-design of Transformer on FPGA Through Sparse Attention and Dynamic Pipelining](https://arxiv.org/abs/2208.03646) |
| 2022 | [Accelerating Attention through Gradient-Based Learned Runtime Pruning](https://arxiv.org/abs/2204.03227) |
| 2022 | [Adaptable Butterfly Accelerator for Attention-based NNs via Hardware and Algorithm Co-design](https://arxiv.org/abs/2209.09570) |
| 2022 | [CPSAA: Accelerating Sparse Attention using Crossbar-based Processing-In-Memory Architecture](https://arxiv.org/abs/2210.06696) |
| 2022 | [DOTA: Detect and Omit Weak Attentions for Scalable Transformer Acceleration](https://researchportal.hkust.edu.hk/en/publications/dota-detect-and-omitweak-attentions-for-scalable-transformer-acce/) |
| 2022 | [SALO: An Efficient Spatial Accelerator Enabling Hybrid Sparse Attention Mechanisms for Long Sequences](https://arxiv.org/abs/2206.14550) |
| 2022 | [Sparse Attention Acceleration with Synergistic In-Memory Pruning and On-Chip Recomputation](https://arxiv.org/abs/2209.00606) |
| 2025 | [Designing Spatial Architectures for Sparse Attention: STAR Accelerator via Cross-Stage Tiling](https://arxiv.org/abs/2512.20198) |
| 2025 | [PADE: A Predictor-Free Sparse Attention Accelerator via Unified Execution and Stage Fusion](https://arxiv.org/abs/2512.14322) |
| 2026 | [Dynamic Sparse Attention: Access Patterns and Architecture](https://arxiv.org/abs/2603.13430) |
| 2026 | [FAST-Prefill: FPGA Accelerated Sparse Attention for Long Context LLM Prefill](https://arxiv.org/abs/2602.20515) |
| 2026 | [Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention](https://arxiv.org/abs/2608.03555) |
| 2026 | [Salca: A Sparsity-Aware Hardware Accelerator for Efficient Long-Context Attention Decoding](https://arxiv.org/abs/2604.24820) |

# **4. Applications**

Application papers show how sparse attention is adapted to the structure and quality requirements of visual generation tasks.

This chapter discusses task-specific support patterns, temporal or spatial constraints, practical acceleration, memory behavior, and generation quality. Papers are intentionally mapped back to the method taxonomy so that mechanism and application evidence remain connected.

# **4.1 Image Generation and Editing**

Image-generation methods exploit spatial locality, regional structure, multiscale layouts, or autoregressive neighborhoods. Their evaluation emphasizes image quality, prompt alignment, controllability, and high-resolution efficiency.

| Year | Paper Links |
|---:|---|
| 2018 | [Image Transformer](https://arxiv.org/abs/1802.05751) |
| 2019 | [Generating Long Sequences with Sparse Transformers](https://arxiv.org/abs/1904.10509) |
| 2019 | [Your Local GAN: Designing Two Dimensional Local Attention Mechanisms for Generative Models](https://arxiv.org/abs/1911.12287) |
| 2020 | [Efficient Content-Based Sparse Attention with Routing Transformers](https://arxiv.org/abs/2003.05997) |
| 2020 | [Semantic Layout Manipulation with High-Resolution Sparse Attention](https://arxiv.org/abs/2012.07288) |
| 2020 | [Sparse Sinkhorn Attention](https://arxiv.org/abs/2002.11296) |
| 2021 | [CogView: Mastering Text-to-Image Generation via Transformers](https://arxiv.org/abs/2105.13290) |
| 2021 | [Zero-Shot Text-to-Image Generation](https://arxiv.org/abs/2102.12092) |
| 2022 | [DynaST: Dynamic Sparse Transformer for Exemplar-Guided Image Generation](https://arxiv.org/abs/2207.06124) |
| 2025 | [Hilbert-Guided Sparse Local Attention](https://arxiv.org/abs/2511.05832) |
| 2025 | [HilbertA: Hilbert Attention for Image Generation with Diffusion Models](https://arxiv.org/abs/2509.26538) |
| 2025 | [Make It Efficient: Dynamic Sparse Attention for Autoregressive Image Generation](https://arxiv.org/abs/2506.18226) |
| 2025 | [Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers](https://arxiv.org/abs/2512.16615) |
| 2026 | [AccelAes: Accelerating Diffusion Transformers for Training-Free Aesthetic-Enhanced Image Generation](https://arxiv.org/abs/2603.12575) |
| 2026 | [ElasticDiT: Efficient Diffusion Transformers via Elastic Architecture and Sparse Attention for High-Resolution Image Generation on Mobile Devices](https://arxiv.org/abs/2605.15684) |
| 2026 | [SDiT: Semantic Region-Adaptive for Diffusion Transformers](https://arxiv.org/abs/2601.12283) |
| 2026 | [SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration](https://arxiv.org/abs/2602.04361) |

# **4.2 Video Generation and Editing**

Video-generation methods combine spatial and temporal sparsity. Their support must preserve motion, identity, temporal consistency, and long-range dependencies while controlling the cost of large spatiotemporal token sequences.

## **4.2.1 General Video Generation**

General video-generation methods accelerate standard text-to-video, image-to-video, and video-diffusion workloads across common durations and resolutions.

| Year | Paper Links |
|---:|---|
| 2022 | [Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation](https://arxiv.org/abs/2212.11565) |
| 2023 | [Photorealistic Video Generation with Diffusion Models](https://arxiv.org/abs/2312.06662) |
| 2024 | [Open-Sora: Democratizing Efficient Video Production for All](https://arxiv.org/abs/2412.20404) |
| 2025 | [Bidirectional Sparse Attention for Faster Video Diffusion Training](https://arxiv.org/abs/2509.01085) |
| 2025 | [BLADE: Block-Sparse Attention Meets Step Distillation for Efficient Video Generation](https://arxiv.org/abs/2508.10774) |
| 2025 | [DraftAttention: Fast Video Diffusion via Low-Resolution Attention Guidance](https://arxiv.org/abs/2505.14708) |
| 2025 | [Efficient-vDiT: Efficient Video Diffusion Transformers With Attention Tile](https://arxiv.org/abs/2502.06155) |
| 2025 | [Fast Video Generation with Sliding Tile Attention](https://arxiv.org/abs/2502.04507) |
| 2025 | [FG-Attn: Leveraging Fine-Grained Sparse Attention in Video Diffusion Models](https://arxiv.org/abs/2509.16518) |
| 2025 | [FPSAttention: Training-Aware FP8 and Sparsity Co-Design for Fast Video Diffusion](https://arxiv.org/abs/2506.04648) |
| 2025 | [LiteAttention: A Temporal Sparse Attention for Diffusion Transformers](https://arxiv.org/abs/2511.11062) |
| 2025 | [QuantSparse: Comprehensively Compressing Video Diffusion Transformer with Model Quantization and Attention Sparsification](https://arxiv.org/abs/2509.23681) |
| 2025 | [RainFusion: Adaptive Video Generation Acceleration via Multi-Dimensional Visual Redundancy](https://arxiv.org/abs/2505.21036) |
| 2025 | [Rectified SpaAttn: Revisiting Attention Sparsity for Efficient Video Generation](https://arxiv.org/abs/2511.19835) |
| 2025 | [SLA: Beyond Sparsity in Diffusion Transformers via Fine-Tunable Sparse-Linear Attention](https://arxiv.org/abs/2509.24006) |
| 2025 | [Sparse VideoGen: Accelerating Video Diffusion Transformers with Spatial-Temporal Sparsity](https://arxiv.org/abs/2502.01776) |
| 2025 | [Sparse VideoGen2: Accelerate Video Generation with Sparse Attention via Semantic-Aware Permutation](https://arxiv.org/abs/2505.18875) |
| 2025 | [Sparse-vDiT: Unleashing the Power of Sparse Attention to Accelerate Video Diffusion Transformers](https://arxiv.org/abs/2506.03065) |
| 2025 | [Training-Free Efficient Video Generation via Dynamic Token Carving](https://arxiv.org/abs/2505.16864) |
| 2025 | [USV: Unified Sparsification for Accelerating Video Diffusion Models](https://arxiv.org/abs/2512.05754) |
| 2025 | [VORTA: Efficient Video Diffusion via Routing Sparse Attention](https://arxiv.org/abs/2505.18809) |
| 2025 | [VSA: Faster Video Diffusion with Trainable Sparse Attention](https://arxiv.org/abs/2505.13389) |
| 2026 | [Accelerating Text-to-Video Generation with Calibrated Sparse Attention](https://arxiv.org/abs/2603.05503) |
| 2026 | [AdaCluster: Adaptive Query-Key Clustering for Sparse Attention in Video Generation](https://arxiv.org/abs/2604.18348) |
| 2026 | [Attention Sparsity is Input-Stable: Training-Free Sparse Attention for Video Generation via Offline Sparsity Profiling and Online QK Co-Clustering](https://arxiv.org/abs/2603.18636) |
| 2026 | [DFSAttn: Dynamic Fine-grained Sparse Attention for Efficient Video Generation](https://arxiv.org/abs/2605.23445) |
| 2026 | [FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation](https://arxiv.org/abs/2607.16190) |
| 2026 | [HEART: Exploiting Head Heterogeneity in Sparse Attention for Video Diffusion](https://arxiv.org/abs/2605.14513) |
| 2026 | [LoSA: Near-Lossless Sparse Attention for Training-Free Video Diffusion Acceleration](https://arxiv.org/abs/2608.12032) |
| 2026 | [Mixture of Distributions Matters: Dynamic Sparse Attention for Efficient Video Diffusion Transformers](https://arxiv.org/abs/2601.11641) |
| 2026 | [OSP-Next: Efficient High-Quality Video Generation with Sparse Sequence Parallelism, HiF8 Quantization, and Reinforcement Learning](https://arxiv.org/abs/2605.28691) |
| 2026 | [RAPID: Reusing Attention Sparsity with Inter-step Adaptation for Efficient Video Diffusion](https://openaccess.thecvf.com/content/CVPR2026/papers/Lin_RAPID_Reusing_Attention_Sparsity_with_Inter-step_Adaptation_for_Efficient_Video_CVPR_2026_paper.pdf) |
| 2026 | [Ride the Wave: Precision-Allocated Sparse Attention for Smooth Video Generation](https://arxiv.org/abs/2604.12219) |
| 2026 | [SALAD: Achieve High-Sparsity Attention via Efficient Linear Attention Tuning for Video Diffusion Transformer](https://arxiv.org/abs/2601.16515) |
| 2026 | [ScalingAttention: Discovering Intrinsic Sparse Attention Topology for Video Diffusion Transformers](https://arxiv.org/abs/2606.23019) |
| 2026 | [SCOPE: Subspace Clustering with Online Per-Head Top-K Estimation for Sparse Video Attention](https://arxiv.org/abs/2608.12780) |
| 2026 | [Sol-Attn: Accelerating Video Generation Inference via On-the-Fly Attention Sparsification](https://arxiv.org/abs/2607.24027) |
| 2026 | [SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference](https://arxiv.org/abs/2608.03335) |
| 2026 | [SVG-EAR: Parameter-Free Linear Compensation for Sparse Video Generation via Error-aware Routing](https://arxiv.org/abs/2603.08982) |
| 2026 | [Token Radius Attention for Efficient Video Generation](https://arxiv.org/abs/2608.02504) |
| 2026 | [Training-free sparse attention based on cumulative energy filtering](https://arxiv.org/abs/2606.16317) |
| 2026 | [VMonarch: Efficient Video Diffusion Transformers with Structured Attention](https://arxiv.org/abs/2601.22275) |

## **4.2.2 Long Video Generation**

Long-video methods emphasize long-range temporal consistency, memory growth, chunk interaction, and sparse support across extended sequences.

| Year | Paper Links |
|---:|---|
| 2024 | [Open-Sora Plan: Open-Source Large Video Generation Model](https://arxiv.org/abs/2412.00131) |
| 2025 | [Compact Attention: Exploiting Structured Spatio-Temporal Sparsity for Fast Video Generation](https://arxiv.org/abs/2508.12969) |
| 2025 | [HoloCine: Holistic Generation of Cinematic Multi-Shot Long Video Narratives](https://arxiv.org/abs/2510.20822) |
| 2025 | [LongCat-Video Technical Report](https://arxiv.org/abs/2510.22200) |
| 2025 | [Mixture of Contexts for Long Video Generation](https://arxiv.org/abs/2508.21058) |
| 2025 | [MoGA: Mixture-of-Groups Attention for End-to-End Long Video Generation](https://arxiv.org/abs/2510.18692) |
| 2025 | [Radial Attention: $O(n\\log n)$ Sparse Attention with Energy Decay for Long Video Generation](https://arxiv.org/abs/2506.19852) |
| 2025 | [Training-free and Adaptive Sparse Attention for Efficient Long Video Generation](https://arxiv.org/abs/2502.21079) |
| 2025 | [VMoBA: Mixture-of-Block Attention for Video Diffusion Models](https://arxiv.org/abs/2506.23858) |
| 2026 | [DynamicRad: Content-Adaptive Sparse Attention for Long Video Diffusion](https://arxiv.org/abs/2604.20470) |
| 2026 | [HyperVAttention: Efficient Sparse Attention with Spatio-Temporal Clustering for Video Diffusion](https://arxiv.org/abs/2607.03012) |
| 2026 | [LVSA: Training-Free Sparse Attention for Long Video Diffusion](https://arxiv.org/abs/2605.31057) |
| 2026 | [Veda: Scalable Video Diffusion via Distilled Sparse Attention](https://arxiv.org/abs/2605.30325) |

## **4.2.3 Autoregressive and Streaming Generation**

Autoregressive and streaming methods select sparse support under causal, incremental, or real-time generation constraints.

| Year | Paper Links |
|---:|---|
| 2021 | [GODIVA: Generating Open-DomaIn Videos from nAtural Descriptions](https://arxiv.org/abs/2104.14806) |
| 2021 | [VideoGPT: Video Generation using VQ-VAE and Transformers](https://arxiv.org/abs/2104.10157) |
| 2022 | [NUWA-Infinity: Autoregressive over Autoregressive Generation for Infinite Visual Synthesis](https://arxiv.org/abs/2207.09814) |
| 2026 | [Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention](https://arxiv.org/abs/2602.04789) |
| 2026 | [MonarchRT: Efficient Attention for Real-Time Video Generation](https://arxiv.org/abs/2602.12271) |
| 2026 | [Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/abs/2604.21221) |
| 2026 | [SparSTAR: Sparse Attention for SpaceTime AutoRegressive Video Synthesis](https://arxiv.org/abs/2608.10519) |

## **4.2.4 Other Video Tasks and Cross-Scenario Support**

This group covers video editing, control, insertion, unified image-video generation, sparse sequence parallelism, and other task-specific video settings.

| Year | Paper Links |
|---:|---|
| 2021 | [NÜWA: Visual Synthesis Pre-training for Neural visUal World creAtion](https://arxiv.org/abs/2111.12417) |
| 2025 | [db-SP: Accelerating Sparse Attention for Visual Generative Models with Dual-Balanced Sequence Parallelism](https://arxiv.org/abs/2511.23113) |
| 2025 | [DiTVR: Zero-Shot Diffusion Transformer for Video Restoration](https://arxiv.org/abs/2508.07811) |
| 2025 | [DSV: Exploiting Dynamic Sparsity to Accelerate Large-Scale Video DiT Training](https://arxiv.org/abs/2502.07590) |
| 2025 | [FlashOmni: A Unified Sparse Attention Engine for Diffusion Transformers](https://arxiv.org/abs/2509.25401) |
| 2025 | [PSA: Pyramid Sparse Attention for Efficient Video Understanding and Generation](https://arxiv.org/abs/2512.04025) |
| 2026 | [Chorus II: Cross-Request Sparsity Reuse for Efficient Image-to-Video Generation](https://arxiv.org/abs/2606.25040) |
| 2026 | [DSA: Efficient Inference For Video Generation Models via Distributed Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2026/file/c3728248f3c627d1f16ca5726cdf83f5-Paper-Conference.pdf) |
| 2026 | [LIVEditor-14B: Lightning Unified Video Editing via In-Context Sparse Attention](https://arxiv.org/abs/2605.04569) |
| 2026 | [SimInsert: Seamless Video Object Insertion via Regional Sparse Attention Fusion](https://arxiv.org/abs/2605.23245) |
| 2026 | [Sol Video Inference Engine: Agent-Native Full-Stack Acceleration Framework for Efficient Video Generation](https://arxiv.org/abs/2606.23743) |
| 2026 | [VecAttention: Vector-wise Sparse Attention for Accelerating Long Context Inference](https://arxiv.org/abs/2603.29494) |

# **4.3 World Models and Interactive Visual Generation**

World-model methods use sparse attention to model long action-observation histories, interactive environments, embodied trajectories, and temporally extended visual dynamics.

| Year | Paper Links |
|---:|---|
| 2025 | [GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861) |
| 2026 | [Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention](https://arxiv.org/abs/2602.01801) |
| 2026 | [Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players](https://arxiv.org/abs/2605.28816) |
| 2026 | [Geometry-Aware Rotary Position Embedding for Consistent Video World Model](https://arxiv.org/abs/2602.07854) |
| 2026 | [Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models](https://arxiv.org/abs/2605.31158) |
| 2026 | [MotionCraft: Latent World Modeling with Sparse Attention for Visual Upscaling](https://arxiv.org/abs/2608.08553) |
| 2026 | [Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models](https://arxiv.org/abs/2608.18484) |
| 2026 | [ReWorld: An Interactive World Model with Long-Horizon Memory](https://arxiv.org/abs/2608.23565) |
| 2026 | [Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037) |
| 2026 | [X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling](https://arxiv.org/abs/2605.24892) |

# **4.4 3D/4D Visual Generation**

3D/4D methods exploit geometric neighborhoods, view consistency, spatial structures, point or voxel organization, and temporal deformation to define efficient attention support.

| Year | Paper Links |
|---:|---|
| 2025 | [Articulate That Object Part (ATOP): 3D Part Articulation via Text and Motion Personalization](https://arxiv.org/abs/2502.07278) |
| 2025 | [Direct3D-S2: Gigascale 3D Generation Made Easy with Spatial Sparse Attention](https://arxiv.org/abs/2505.17412) |
| 2026 | [AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model](https://arxiv.org/abs/2604.19747) |
| 2026 | [Full-4D: Generating Full-Scope 4D Scenes from a Single-View Video](https://arxiv.org/abs/2605.25500) |
| 2026 | [Helix4D: Complex 4D Mesh Generation](https://arxiv.org/abs/2605.26109) |
| 2026 | [LSRM: High-Fidelity Object-Centric Reconstruction via Scaled Context Windows](https://arxiv.org/abs/2604.05182) |
| 2026 | [Sculpt4D: Generating 4D Shapes via Sparse-Attention Diffusion Transformers](https://arxiv.org/abs/2604.21592) |
| 2026 | [Z-Order Transformer for Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2605.13465) |

# **4.5 Portrait and Audio-Visual Generation**

Portrait and audio-visual methods connect speech, audio events, facial motion, identity, and video frames. Sparse support is used to retain cross-modal synchronization while reducing temporal attention cost.

| Year | Paper Links |
|---:|---|
| 2022 | [MM-Diffusion: Learning Multi-Modal Diffusion Models for Joint Audio and Video Generation](https://arxiv.org/abs/2212.09478) |
| 2025 | [Input-Aware Sparse Attention for Real-Time Co-Speech Video Generation](https://arxiv.org/abs/2510.02617) |
| 2025 | [TalkingMachines: Real-Time Audio-Driven FaceTime-Style Video via Autoregressive Diffusion Models](https://arxiv.org/abs/2506.03099) |
| 2026 | [Avatar V: Scaling Video-Reference Avatar Video Generation](https://arxiv.org/abs/2606.13872) |
| 2026 | [Efficient Audio-Visual Generation via Synchrony-Aware Cross-Modal Sparse Attention](https://arxiv.org/abs/2608.15522) |
| 2026 | [Hallo-Live: Real-Time Streaming Joint Audio-Video Avatar Generation with Asynchronous Dual-Stream and Human-Centric Preference Distillation](https://arxiv.org/abs/2604.23632) |
| 2026 | [Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](https://arxiv.org/abs/2608.23383) |
| 2026 | [Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](https://arxiv.org/abs/2608.05663) |



