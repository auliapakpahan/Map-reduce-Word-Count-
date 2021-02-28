# Word count using MapReduce in python
MapReduce is a programming model designed to be able to process very large amounts of data by dividing the processing into several independent tasks. The MapReduce workflow consists of the following four steps:
1. Splitting,
At this stage the input provided by the user will be broken down into several parts. The parameters used to carry out the splitting stage can be space, comma, semicolon, or new line.
2. Mapping,
At the mapping stage, the split data will be mapped into tuples (key-value pairs).
3. Intermediate Splitting,
At this stage the tuples that have been formed at the mapping stage will be grouped based on the same key.
4. Reduce,
In the reduce stage, all key and value pairs will be aggregated based on the same key.
