#pragma once

#include <vector>

using std::vector;

namespace two_bucket {

enum class bucket_id { one, two };

struct measure_result {
    int num_moves;
    bucket_id goal_bucket;
    int other_bucket_volume;
};

struct BFS_node {
    int bucket1 = 0;
    int bucket2 = 0;
    measure_result result; 
};

BFS_node transferAB(BFS_node node, int bucket1_capacity);
BFS_node transferBA(BFS_node node, int bucket2_capacity);
BFS_node emptyA(BFS_node node);
BFS_node emptyB(BFS_node node);
BFS_node fillA(BFS_node node, int bucket1_capacity);
BFS_node fillB(BFS_node node, int bucket2_capacity);
// bool check_found(BFS_node node, int target_volume, measure_result& result, bool& found, int& i);

void update_result(measure_result& result, int target_volume, BFS_node node_next, int num_moves);
void update_next_nodes(BFS_node node_next, vector<std::pair<int,int>>& visited, vector<BFS_node>& next_nodes);
measure_result graph_BFS(const vector<BFS_node>& nodes, int bucket1_capacity, int bucket2_capacity, int target_volume, bucket_id start_bucket, measure_result& result, int num_moves, vector<std::pair<int,int>>& visited);

measure_result measure(int bucket1_capacity, int bucket2_capacity, int target_volume, bucket_id start_bucket);

}  // namespace two_bucket
