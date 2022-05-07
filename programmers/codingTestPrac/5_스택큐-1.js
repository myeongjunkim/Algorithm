function solution(progresses, speeds) {
    
    let result = [];
    
    while(progresses.length !=0){
        while(progresses[0] <100){
//            진도율 더하기
            for(let j=0; j<progresses.length; j++){
                progresses[j] += speeds[j]
            }
        }
        let cnt = 0;
        while(progresses[0] >= 100){
            progresses.shift();
            speeds.shift();
            cnt++;
        }
        result.push(cnt);
        
    }
    return result;
}