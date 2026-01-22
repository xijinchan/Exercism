import random
import itertools

def measure(bucket_one, bucket_two, goal, start_bucket):
    global actions
    global bucket_A, bucket_B
    global sequence
    
    class Bucket:
        def __init__(self, bucket_number):
            self.bucket_number = bucket_number
            self.capacity = None
            self.level = 0

    def reset():
        global actions
        global bucket_A, bucket_B
        global sequence
        if start_bucket == 'one':
            bucket_A, bucket_B = Bucket('one'), Bucket('two')
            bucket_A.capacity, bucket_B.capacity = bucket_one, bucket_two
        else:
            bucket_A, bucket_B = Bucket('two'), Bucket('one')
            bucket_A.capacity, bucket_B.capacity = bucket_two, bucket_one
        actions = 0
        sequence = []

    if goal > bucket_one and goal > bucket_two:
        raise ValueError('goal must be smaller than either bucket')
    reset()

    def fill(bucket):
        global actions 
        bucket.level = bucket.capacity
        actions += 1
        
    def empty(bucket):
        global actions
        bucket.level = 0
        actions += 1

    def pour(bucket_A, bucket_B):
        global actions
        bucket_B_level_original = bucket_B.level
        bucket_B.level = min(bucket_A.level + bucket_B.level, bucket_B.capacity)
        bucket_A.level = max(bucket_A.level - (bucket_B.level - bucket_B_level_original), 0)
        actions += 1

    def check():
        if bucket_A.level == goal or bucket_B.level == goal:
            goal_bucket = bucket_A.bucket_number if bucket_A.level is goal else bucket_B.bucket_number
            other_bucket_level = bucket_B.level if bucket_A.level is goal else bucket_A.level
            return (actions, goal_bucket, other_bucket_level)

    def solve():
            
        while True:
            fill(bucket_A)
            if check(): return check()
            if bucket_B.capacity == goal:
                fill(bucket_B)
                return check()
            if bucket_A.level == 0 and bucket_B.level == bucket_B.capacity: break
            pour(bucket_A, bucket_B)
            if check(): return check()
            if bucket_A.level == 0 and bucket_B.level == bucket_B.capacity: break
            if bucket_B.level == bucket_B.capacity:
                empty(bucket_B)
                if bucket_A.level == 0 and bucket_B.level == bucket_B.capacity: break
                pour(bucket_A, bucket_B)
                if check(): return check()
                if bucket_A.level == 0 and bucket_B.level == bucket_B.capacity: break
                if bucket_B.level == bucket_B.capacity:
                    empty(bucket_B)
                    if bucket_A.level == 0 and bucket_B.level == bucket_B.capacity: break
                    pour(bucket_A, bucket_B)
                    if check(): return check()
                    if bucket_A.level == 0 and bucket_B.level == bucket_B.capacity: break

    solution = solve()
    if solution:
        return solution
    else:
        raise ValueError('No solution found')

            # fill(bucket_A)
            # if bucket_B.capacity == goal: fill(bucket_B)
            # pour(bucket_A, bucket_B)
            # if bucket_B.level == bucket_B.capacity:
            #     empty(bucket_B)
            #     pour(bucket_A, bucket_B)
            #     if bucket_B.level == bucket_B.capacity:
            #         empty(bucket_B)
            #         pour(bucket_A, bucket_B)

        # A B
        # 3 5
        # 3 0 fill A
        # 0 3 pour A to B
        # 3 3 fill A
        # 1 5 pour A to B, B full
        # 1 0 empty B
        # 0 1 pour A to B
        # 3 1 fill A
        # 0 4 pour A to B
        # 3 4 fill A
        # 2 5 pour A to B, B full
        # 2 0 empty B
        # 0 2 pour A to B
        # 3 2 fill A
        # 0 5 fin, disallowed
 
        # B A
        # 3 5
        # 0 5 fill A
        # 3 2 pour A to B, B filled
        # 0 2 empty B
        # 2 0 pour A to B
        # 2 5 fill A
        # 3 4 pour A to B, B filled
        # 0 4 empty B
        # 3 1 pour A to B, B filled
        # 0 1 empty B
        # 1 0 pour A to B
        # 1 5 fill A
        # 3 3 pour A to B
        # 0 3 empty B
        # 3 0 pour A to B, fin disallowed
    
    # def solve():
    
    # def fill(bucket):
    #     global actions
    #     bucket.level = bucket.capacity
    #     actions += 1
        
    # def empty(bucket):
    #     global actions
    #     bucket.level = 0
    #     actions += 1

    # def pour(bucket_A, bucket_B):
    #     global actions
    #     bucket_B_level_original = bucket_B.level
    #     bucket_B.level = min(bucket_A.level + bucket_B.level, bucket_B.capacity)
    #     bucket_A.level = max(bucket_A.level - (bucket_B.level - bucket_B_level_original), 0)
    #     actions += 1
    
    # def solve(): # random step generation
    #     global bucket_A, bucket_B, actions
    #     reset()
    #     actions = 0
    #     functions = [
    #         lambda: fill(bucket_A), lambda: fill(bucket_B),
    #         lambda: empty(bucket_A), lambda: empty(bucket_B),
    #         lambda: pour(bucket_A, bucket_B), lambda: pour(bucket_B, bucket_A)]
    #     sequence = []

    #     def check():
    #         if bucket_A.level == goal or bucket_B.level == goal:
    #             goal_bucket = bucket_A.bucket_number if bucket_A.level is goal else bucket_B.bucket_number
    #             other_bucket_level = bucket_B.level if bucket_A.level is goal else bucket_A.level
    #             # print((actions, goal_bucket, other_bucket_level, sequence))
    #             return (actions, goal_bucket, other_bucket_level, sequence)

    #     fill(bucket_A)
    #     sequence.append(0)
    #     func = functions[0]
    #     if check():
    #         return check()
        
    #     for i in range(20):
    #         # exclude actions from current loop
    #         prohibited_subsequent = [
    #             functions[2], functions[3],
    #             functions[4], functions[5],
    #             functions[5], functions[4]]
    #         prohibited = set()
    #         if func != None:
    #             if prohibited_subsequent[functions.index(func)] != None:
    #                 prohibited.add(prohibited_subsequent[functions.index(func)])
    #             if functions.index(func) not in [4,5]:
    #                 prohibited.add(func) # prohibit repetition
    #         if bucket_A.level == 0:
    #             prohibited.add(functions[2])
    #         if bucket_B.level == 0:
    #             prohibited.add(functions[3])
    #         if bucket_A.level == bucket_A.capacity:
    #             prohibited.add(functions[0])
    #             prohibited.add(functions[1])
    #             prohibited.add(functions[5])
    #         if bucket_B.level == bucket_B.capacity:
    #             prohibited.add(functions[0])
    #             prohibited.add(functions[1])
    #             prohibited.add(functions[4])
    #         '''
    #         to-do:
    #         prohibit
    #         After an action, you may not arrive at a state where the starting bucket is empty and the other bucket is full.
    #         ''' 
    #         before_level_A, before_level_B = bucket_A.level, bucket_B.level 
    #         for k in range(20):
    #             # print('prohibited = ',[functions.index(k) for k in prohibited])
    #             func = random.choice([f for f in functions if f not in prohibited])
    #             # print('trying func',functions.index(func))
    #             func()
    #             if bucket_A.level == 0 and bucket_B.level == bucket_B.capacity:
    #                 bucket_A.level, bucket_B.level = before_level_A, before_level_B
    #                 actions -= 1
    #                 continue
    #             else:
    #                 break
            
    #         sequence.append(functions.index(func))
    #         # print('func, A, B = ',functions.index(func), bucket_A.level, bucket_B.level)
    #         # print('sequence = ',sequence)

    #         if check():
    #             return check()

    # solution = None
    
    # # for k in range(200):
    # #     attempt = solve()
    # #     if attempt:
    # #         if solution == None:
    # #             solution = attempt
    # #             print(solution)
    # #         if attempt[0] < solution[0]:
    # #             solution = attempt
    # #             print(solution)
    # #             print(k)

    # # return solution[:-1]

    # import itertools

    # def fill(bucket):
    #     global actions
    #     bucket.level = bucket.capacity
    #     actions += 1
    #     if check():
    #         return check()
        
    # def empty(bucket):
    #     global actions
    #     bucket.level = 0
    #     actions += 1
    #     if check():
    #         return check()

    # def pour(bucket_A, bucket_B):
    #     global actions
    #     bucket_B_level_original = bucket_B.level
    #     bucket_B.level = min(bucket_A.level + bucket_B.level, bucket_B.capacity)
    #     bucket_A.level = max(bucket_A.level - (bucket_B.level - bucket_B_level_original), 0)
    #     actions += 1
    #     if check():
    #         return check()

    # def check():
    #     global sequence
    #     if bucket_A.level == goal or bucket_B.level == goal:
    #         goal_bucket = bucket_A.bucket_number if bucket_A.level is goal else bucket_B.bucket_number
    #         other_bucket_level = bucket_B.level if bucket_A.level is goal else bucket_A.level
    #         # print((actions, goal_bucket, other_bucket_level, sequence))
    #         return (actions, goal_bucket, other_bucket_level)
    
    # def solve_2(): # iterative generation
    #     global bucket_A, bucket_B, actions
    #     global sequence
    #     reset()
    #     actions = 0
    #     functions = [
    #         lambda: fill(bucket_A), lambda: fill(bucket_B),
    #         lambda: empty(bucket_A), lambda: empty(bucket_B),
    #         lambda: pour(bucket_A, bucket_B), lambda: pour(bucket_B, bucket_A)]
    #     sequence = []

    #     fill(bucket_A)
    #     sequence.append(0)
    #     func = functions[0]
    #     if check():
    #         return check()

    #     def go_through_funcs(functions_indices):
    #         global sequence
    #         for k in functions_indices:
    #             if bucket_B.level == 0 and k == 3:
    #                 break
    #             if bucket_A.level == bucket_A.capacity and k in [0,5]:
    #                 break
    #             if bucket_B.level == bucket_B.capacity and k in [1,4]:
    #                 break
                    
    #             functions[k]()
    #             if bucket_A.level == 0 and bucket_B.level == bucket_B.capacity:
    #                 break
    #             sequence.append(k)
    #         if check():
    #             return check()
    #         else:
    #             reset()
    #             fill(bucket_A)
    #             sequence.append(0)

    #     prohibited = [
    #         [0,2], [1,3],
    #         [2,4], [3,5],
    #         [4,5], [5,4],
    #         [0,0], [1,1],
    #         [2,2], [3,3]
    #     ]
    #     # prohibited = [
    #         # fill then empty,
    #         # empty then pour,
    #         # pour A-B then B-A,
    #         # repeat fill,
    #         # repeat empty
    #     # ]

    #     solution = ((A)
    #                 for (A) in itertools.product(range(6), repeat=1)
    #                 # if functions[A[0]]() is not None
    #                 if go_through_funcs((A)) is not None
    #                )
    #     try:
    #         next(solution)
    #         if solution:
    #             output = check()
    #             print('solution! = ', output)
    #             return output
    #     except:
    #         solution = ((A,B,C)
    #                     for (A,B,C) in itertools.product(range(6), repeat=3)
    #                     if not [(A,B,C)[k:k+2] for k in range(len((A,B,C)[:-1])) if (A,B,C)[k:k+2] in prohibited]
    #                     if go_through_funcs((A,B,C)) is not None
    #                    )
    #         try:
    #             next(solution)
    #             if solution:
    #                 output = check()
    #                 print('solution! = ', output)
    #                 return output
    #         except:
    #             print('try 7')
    #             solution = ((A,B,C,D,E,F,G)
    #                         for (A,B,C,D,E,F,G) in itertools.product(range(6), repeat=7)
    #                         if not [(A,B,C,D,E,F,G)[k:k+2] for k in range(len((A,B,C,D,E,F,G)[:-1])) if (A,B,C,D,E,F,G)[k:k+2] in prohibited]
    #                         if go_through_funcs((A,B,C,D,E,F,G)) is not None
    #                        )
    #             try:
    #                 next(solution)
    #                 if solution:
    #                     output = check()
    #                     print('solution! = ', output, sequence)
    #                     return output
    #             except:
    #                 print('except!')
    #                 # print('try 13')
    #                 # solution = ((A,B,C,D,E,F,G,H,I,J,K,L,M)
    #                 #             for (A,B,C,D,E,F,G,H,I,J,K,L,M) in itertools.product(range(6), repeat=13)
    #                 #             if not [(A,B,C,D,E,F,G,H,I,J,K,L,M)[k:k+2] for k in range(len((A,B,C,D,E,F,G,H,I,J,K,L,M)[:-1])) if (A,B,C,D,E,F,G,H,I,J,K,L,M)[k:k+2] in prohibited]
    #                 #             if go_through_funcs((A,B,C,D,E,F,G,H,I,J,K,L,M)) is not None
    #                 #            )
    #                 # try:
    #                 #     next(solution)
    #                 #     if solution:
    #                 #         output = check()
    #                 #         print('solution! = ', output)
    #                 #         return output[:-1]
    #                 # except:
    #                 #     print('except!')

    # return solve_2()