 // q_insert(q, n_source);
    // while(!q_is_empty(q)){
    //     pos = q_popleft(q);
    //     printf("poppoppop : %d", pos);
    //     for(int i=0; i<MAX_QUEUE_SIZE; i++){
    //         int nearby_index = gragh[pos][i];
    //         if(!node_case[nearby_index].visited){
    //             node_case[nearby_index].visited = 1;
    //             node_case[nearby_index].d_source += node_case[pos].d_source;
    //             node_case[nearby_index].pre_node = pos;
    //             q_insert(q, nearby_index);
    //         }
    //     }
    // }