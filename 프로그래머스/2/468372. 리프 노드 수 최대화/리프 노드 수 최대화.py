# 2발, 3발
def solution(dist_limit, split_limit):
    def get_max_count(dist_limit, split_limit):
        max_count = 1
        stack = [(1, dist_limit, 0)]
        while stack:
            leaf_node_count, dist_limit, depth = stack.pop()
            max_count = max(max_count, leaf_node_count)
            leaf_node_count_2 = leaf_node_count * 2
            if leaf_node_count_2 <= split_limit:
                if dist_limit - leaf_node_count >= 0:
                    stack.append((leaf_node_count_2, dist_limit - leaf_node_count, depth + 1))
                else:
                    max_count = max(max_count, dist_limit + leaf_node_count)

            leaf_node_count_3 = leaf_node_count * 3
            if leaf_node_count_3 <= split_limit:
                if dist_limit - leaf_node_count >= 0:
                    stack.append((leaf_node_count_3, dist_limit - leaf_node_count, depth + 1))
                else:
                    max_count = max(max_count, dist_limit * 2 + leaf_node_count)
        
        return max_count
                
    def get_depth_count(dist_limit, split_limit):
        stack = [(1, dist_limit, split_limit)]
        count = 1
        while stack:
            limit, dist_limit, split_limit = stack.pop()
            if dist_limit == 0:
                continue
            limit_3 = limit * 3
            if limit_3 <= split_limit:
                count += 2
                stack.append((limit_3, dist_limit - 1, split_limit))
            elif limit * 2 <= split_limit and dist_limit:
                count += 1
                
        return count
            
    max_count, count = get_max_count(dist_limit, split_limit), get_depth_count(dist_limit, split_limit)
    # print(max_count, count)
    answer = max(max_count, count)
    return answer