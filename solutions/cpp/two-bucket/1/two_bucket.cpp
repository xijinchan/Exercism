#include "two_bucket.h"

#include <algorithm>
#include <stdexcept>

namespace two_bucket {

// TODO: add your solution here
    BFS_node transferAB(BFS_node node, int bucket2_capacity) {
        if (node.bucket1 + node.bucket2  > bucket2_capacity) {
            node.bucket1 -= (bucket2_capacity - node.bucket2);
            node.bucket2 = bucket2_capacity;
        } else {
            node.bucket2 += node.bucket1;
            node.bucket1 = 0;
        }
        return node;
    }
    
    BFS_node transferBA(BFS_node node, int bucket1_capacity) {
        if (node.bucket2 + node.bucket1  > bucket1_capacity) {
            node.bucket2 -= (bucket1_capacity - node.bucket1);
            node.bucket1 = bucket1_capacity;
        } else {
            node.bucket1 += node.bucket2;
            node.bucket2 = 0;
        }
        return node;
    }
    
    BFS_node emptyA(BFS_node node) {        
        node.bucket1 = 0;
        return node;
    }
    
    BFS_node emptyB(BFS_node node) {        
        node.bucket2 = 0;
        return node;
    }
    
    BFS_node fillA(BFS_node node, int bucket1_capacity) {
        node.bucket1 = bucket1_capacity;
        return node;
    }
    
    BFS_node fillB(BFS_node node, int bucket2_capacity) {
        node.bucket2 = bucket2_capacity;
        return node;
    }

    void update_result(measure_result& result, int target_volume, BFS_node node_next, int num_moves) {
        if (node_next.bucket1 == target_volume) {
            result.goal_bucket = two_bucket::bucket_id::one;
            result.other_bucket_volume = node_next.bucket2;
        } else {
            result.goal_bucket = two_bucket::bucket_id::two;
            result.other_bucket_volume = node_next.bucket1;
        }
        result.num_moves = num_moves;
    }

    void update_next_nodes(BFS_node node_next, vector<std::pair<int,int>>& visited, vector<BFS_node>& next_nodes) {
        std::pair<int,int> node_next_pair = {node_next.bucket1, node_next.bucket2};
        auto it = std::find(visited.begin(), visited.end(), node_next_pair);
        if (it == visited.end()) {
            visited.push_back(node_next_pair);
            next_nodes.push_back(node_next);
        }
    }
    
    measure_result measure(int bucket1_capacity, int bucket2_capacity, int target_volume, bucket_id start_bucket) {
        measure_result result;
        BFS_node node_0;
        vector<BFS_node> first_nodes;
        int num_moves = 1;
        vector<std::pair<int,int>> visited;

        // fill start node, add to vector
        if (start_bucket == two_bucket::bucket_id::one) {
            node_0.bucket1 = bucket1_capacity;
            first_nodes.push_back(node_0);
        } else {
            node_0.bucket2 = bucket2_capacity;
            first_nodes.push_back(node_0);
        }

        // check if initial fill solves problem
        if (node_0.bucket1 == target_volume || node_0.bucket2 == target_volume) {
            if (node_0.bucket1 == target_volume) {
                result.goal_bucket = two_bucket::bucket_id::one;
                result.other_bucket_volume = node_0.bucket2;
            } else {
                result.goal_bucket = two_bucket::bucket_id::two;
                result.other_bucket_volume = node_0.bucket1;
            }
            result.num_moves = num_moves;
            return result;
        }

        std::pair<int,int> node_0_pair = {node_0.bucket1, node_0.bucket2};
        visited.push_back(node_0_pair);
        
        result = graph_BFS(first_nodes, bucket1_capacity, bucket2_capacity, target_volume, start_bucket, result, num_moves, visited);
        return result;
    }

        measure_result graph_BFS(const vector<BFS_node>& nodes, int bucket1_capacity, int bucket2_capacity, int target_volume, bucket_id start_bucket, measure_result& result, int num_moves, vector<std::pair<int,int>>& visited) {
            if (target_volume > bucket1_capacity && target_volume > bucket2_capacity) {
                throw std::runtime_error("target_volume greater than both buckets");
            }
            
            num_moves += 1;
            vector<BFS_node> next_nodes;
            BFS_node node_next;
            
            for (BFS_node node: nodes) {
                // transferAB
                if (node.bucket1 != 0 && node.bucket2 != bucket2_capacity) {
                    if (!(start_bucket == two_bucket::bucket_id::one && node.bucket1 - (bucket2_capacity - node.bucket2) == 0)) {
                        node_next = transferAB(node, bucket2_capacity);
                        if (node_next.bucket1 == target_volume || node_next.bucket2 == target_volume) {
                            update_result(result, target_volume, node_next, num_moves);
                            return result;
                        }
                        update_next_nodes(node_next, visited, next_nodes);
                    }
                }
                // emptyA
                if (node.bucket1 != 0) {
                    if (!(start_bucket == two_bucket::bucket_id::one && node.bucket2 == bucket2_capacity)) {
                        node_next = emptyA(node);
                        if (node_next.bucket1 == target_volume || node_next.bucket2 == target_volume) {
                            update_result(result, target_volume, node_next, num_moves);
                            return result;
                        }
                        update_next_nodes(node_next, visited, next_nodes);
                    }
                }
                // fillA
                if (node.bucket1 != bucket1_capacity) {
                    if (!(start_bucket == two_bucket::bucket_id::two && node.bucket2 == 0)) {
                        node_next = fillA(node, bucket1_capacity);
                        if (node_next.bucket1 == target_volume || node_next.bucket2 == target_volume) {
                            update_result(result, target_volume, node_next, num_moves);
                            return result;
                        }
                        update_next_nodes(node_next, visited, next_nodes);
                    }
                }
                // transferBA
                if (node.bucket2 != 0 && node.bucket1 != bucket1_capacity) {
                    if (!(start_bucket == two_bucket::bucket_id::two && node.bucket2 - (bucket1_capacity - node.bucket1) == 0)) {
                        node_next = transferBA(node, bucket1_capacity);
                        if (node_next.bucket1 == target_volume || node_next.bucket2 == target_volume) {
                            update_result(result, target_volume, node_next, num_moves);
                            return result;
                        }
                        update_next_nodes(node_next, visited, next_nodes);
                    }
                }
                // emptyB
                if (node.bucket2 != 0) {
                    if (!(start_bucket == two_bucket::bucket_id::two && node.bucket1 == bucket1_capacity)) {
                        node_next = emptyB(node);
                        if (node_next.bucket1 == target_volume || node_next.bucket2 == target_volume) {
                            update_result(result, target_volume, node_next, num_moves);
                            return result;
                        }
                        update_next_nodes(node_next, visited, next_nodes);
                    }
                }
                // fillB
                if (node.bucket2 != bucket2_capacity) {
                    if (!(start_bucket == two_bucket::bucket_id::one && node.bucket1 == 0)) {
                        node_next = fillB(node, bucket2_capacity);
                        if (node_next.bucket1 == target_volume || node_next.bucket2 == target_volume) {
                            update_result(result, target_volume, node_next, num_moves);
                            return result;
                        }
                        update_next_nodes(node_next, visited, next_nodes);
                    }
                }
            }

            if (next_nodes.empty()) {
                throw std::runtime_error("Not possible!");
            } else {
                // no target found so recursively generate graph_BFS with next layer of nodes
                result = graph_BFS(next_nodes, bucket1_capacity, bucket2_capacity, target_volume, start_bucket, result, num_moves, visited); 
            }
            
            return result;
    }
}  // namespace two_bucket
