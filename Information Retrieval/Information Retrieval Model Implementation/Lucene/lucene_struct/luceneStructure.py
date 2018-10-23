from anytree import NodeMixin, RenderTree
from anytree.exporter import DotExporter
from anytree import Node

class MyClass(NodeMixin):  # Add Node feature
    def __init__(self, name, description, parent=None):
        self.name = name
        self.description = description
        self.parent = parent

#Tree strucutre
lucene = MyClass('Lucene',"")

analysis = MyClass('Analysis', "", parent=lucene)
commonLib = MyClass("Analyzer_Common","Analyzers for indexing content in different languages and domains",parent=analysis)
icuLib = MyClass("Analyzer_Icu","Analyzer integration with ICU (International Components for Unicode)",parent=analysis)
kuromojiLib = MyClass("Analyzer_Kuromoji","Japanese Morphological Analyzer",parent=analysis)
morfologikLib = MyClass("Analyzer_Morfologik","Analyzer for dictionary stemming, built-in Polish dictionary",parent=analysis)
noriLib = MyClass("Analyzer_Nori","Korean Morphological Analyzer",parent=analysis)
opennlpLib = MyClass("Analyzer_OpenNLP","OpenNLP Library Integration",parent=analysis)
phoneticLib = MyClass("Analyzer_Phonetic","Analyzer for indexing phonetic signatures (for sounds-alike search)",parent=analysis)
smartcnLib = MyClass("Analyzer_Smartcn","Analyzer for indexing Chinese",parent=analysis)
stempelLib = MyClass("Analyzer_Stempel","Analyzer for indexing Polish",parent=analysis)
uimaLib = MyClass("Analyzer_Uima","Analysis integration with Apache UIMA",parent=analysis)

backward_codecs = MyClass('Backward_codecs', "", parent=lucene)
backward_codecsLib = MyClass("Backward_Codecs","Codecs for older versions of Lucene.", parent=backward_codecs)

benchmark = MyClass('Benchmark', "", parent=lucene)
benchmarkLib = MyClass('Benchmark', "System for benchmarking Lucene", parent=benchmark)

classfication = MyClass('Classfication', "", parent=lucene)
classficationLib = MyClass('Classfication', "Classification module for Lucene", parent=classfication)

codecs = MyClass('Codecs', "", parent=lucene)
codecsLib = MyClass('Codecs', "Lucene codecs and postings formats.", parent=codecs)

core = MyClass('Core', "", parent=lucene)
coreLib = MyClass('Core', "Lucene core library", parent=core)

demo = MyClass('Demo', "", parent=lucene)
demoLib = MyClass("Demo", "Simple example code",parent=demo)

docs = MyClass('Docs', "", parent=lucene)
docsLib = MyClass('Docs', "Contain all Lucene Java documentations", parent=docs)

expressions = MyClass('Expressions', "", parent=lucene)
expressionsLib = MyClass('Expressions', "Dynamically computed values to sort/facet/search on based on a pluggable grammar.", parent=expressions)

facet = MyClass('Facet', "", parent=lucene)
facetLib = MyClass('Facet', "Faceted indexing and search capabilities", parent=facet)

grouping = MyClass('Grouping', "", parent=lucene)
groupingLib = MyClass('Grouping', "Collectors for grouping search results.", parent=grouping)

highliter = MyClass('Highliter', "", parent=lucene)
highliterLib = MyClass('Highliter', "Highlights search keywords in results", parent=highliter)

join = MyClass('Join', "", parent=lucene)
joinLib = MyClass('Join', "Index-time and Query-time joins for normalized content", parent=join)

licenses = MyClass('Licenses', "", parent=lucene)
licensesLib = MyClass('Licenses', "Contain Lucene Licenses", parent=licenses)

memory = MyClass('Memory', "", parent=lucene)
memoryLib = MyClass('Memory', "Single-document in-memory index implementation", parent=memory)

misc = MyClass('Misc', "", parent=lucene)
miscLib = MyClass('Misc', "Index tools and other miscellaneous code", parent=misc)

queries = MyClass('Queries', "", parent=lucene)
queriesLib = MyClass('Queries', "Filters and Queries that add to core Lucene", parent=queries)

queryparser = MyClass('Queryparser', "", parent=lucene)
queryparserLib = MyClass('Queryparser', "Query parsers and parsing framework", parent=queryparser)

replicator = MyClass('Replicator', "", parent=lucene)
replicatorLib = MyClass('Replicator', "Files replication utility", parent=replicator)

sandbox = MyClass('Sandbox', "", parent=lucene)
sandboxLib = MyClass('Sandbox', "Various third party contributions and new ideas", parent=sandbox)

spatial = MyClass('Spatial', "", parent=lucene)
spatialLib = MyClass('Spatial', "Geospatial search", parent=spatial)

spatial3d = MyClass('Spatial3d', "", parent=lucene)
spatial3dLib = MyClass('Spatial3d', "3D spatial planar geometry APIs", parent=spatial3d)

spatial_extras = MyClass('Spatial_extras', "", parent=lucene)
spatial_extrasLib = MyClass('Spatial_extras', "Geospatial search", parent=spatial_extras)

suggest = MyClass('Suggest', "", parent=lucene)
suggest = MyClass('Suggest', "Auto-suggest and Spellchecking support", parent=suggest)

test_framework = MyClass('Test_framework', "", parent=lucene)
test_framework = MyClass('Test_framework', "Framework for testing Lucene-based applications", parent=test_framework)

for pre, _, node in RenderTree(lucene):
    treestr = u"%s%s" % (pre, node.name)
    print(treestr.ljust(8)+": "+node.description)

DotExporter(lucene).to_dotfile("luceneStructure.dot")
#dot file to png file: dot test.dot -T png -o test.png