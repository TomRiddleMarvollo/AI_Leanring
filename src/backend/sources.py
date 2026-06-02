# sources.py

AI_SOURCES = {
    "Personal Sites": [
        "andrewng.org", "karpathy.ai", "fast.ai", "yann.lecun.com", "fchollet.com", "sebastianraschka.com",
        "people.eecs.berkeley.edu/~jordan", "nlp.stanford.edu/~manning", "cs.stanford.edu/~pliang",
        "people.eecs.berkeley.edu/~russell", "lexfridman.com", "research.google/people/jeff",
        "deepmind.com/people/demis-hassabis", "iangoodfellow.com", "otoro.net", "rohinshah.com",
        "zoubin.com", "schmid.csail.mit.edu", "cs.berkeley.edu/~pabbeel", "cs.berkeley.edu/~svlevine",
        "cs.berkeley.edu/~trevor", "cs.stanford.edu/~ermon", "cs.stanford.edu/~acoates",
        "cs.stanford.edu/~diyiy", "cs.princeton.edu/~blei", "cs.princeton.edu/~li",
        "cs.toronto.edu/~hinton", "yoshua.ca", "cs.nyu.edu/~fergus", "cs.nyu.edu/~roweis",
        "csail.mit.edu/~sanchez"
    ],
    "Research Labs": [
        "deepmind.google/blog", "openai.com/research", "anthropic.com/news", "ai.googleblog.com",
        "ai.meta.com/blog", "research.nvidia.com", "microsoft.com/research/blog",
        "machinelearning.apple.com", "amazon.science", "research.ibm.com", "csail.mit.edu/news",
        "hai.stanford.edu/news", "bair.berkeley.edu/blog", "blog.ml.cmu.edu", "oxford-ai.org/blog",
        "allenai.org/blog", "mila.quebec/en/news", "air.tsinghua.edu.cn", "aida.ust.hk", "ai.ethz.ch"
    ],
    "Code and Tools": [
        "paperswithcode.com", "arxiv-sanity.com", "huggingface.co/blog", "huggingface.co/spaces",
        "kaggle.com/learn", "blog.langchain.dev", "lightning.ai/blog", "keras.io/blog",
        "pytorch.org/blog", "blog.tensorflow.org", "github.com/google/jax", "mlcollective.org",
        "eleuther.ai/blog", "stability.ai/blog", "laion.ai/blog", "huggingface.co/models",
        "github.com/trending", "openmmlab.com", "deeplearning.ai/short-courses", "wandb.ai/articles"
    ],
    "AI Safety": [
        "alignmentforum.org", "lesswrong.com", "safe.ai", "alignment.org", "intelligence.org",
        "governance.ai", "openai.com/safety", "deepmind.google/discover/safety", "crfm.stanford.edu",
        "chai.berkeley.edu", "fhi.ox.ac.uk", "aiethicslab.com", "partnershiponai.org",
        "aigovernance.org", "aisafety.info"
    ],
    "Media": [
        "twitter.com", "medium.com", "linkedin.com", "reddit.com/r/MachineLearning",
        "reddit.com/r/LocalLLaMA", "reddit.com/r/DeepLearning", "news.ycombinator.com",
        "thegradient.pub", "lexfridman.com/podcast", "deeplearning.ai/the-batch", "tldr.tech/ai", "arxiv.org/list/cs.AI/recent"
    ]
}

def get_random_sources(num_sources=3):
    import random
    all_sources = [url for category in AI_SOURCES.values() for url in category]
    return random.sample(all_sources, min(num_sources, len(all_sources)))
