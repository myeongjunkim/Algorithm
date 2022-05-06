function solution(s) {
    
    let caseLen = [];
    for(let per=1; per<s.length/2+1; per++){
        
        let partList = [];
        for(let j=0; j<s.length; j+=per){
            partList.push(s.substr(j,per));
        }
        let lastPart = partList[0];
        let press = "";
        let count = 1
        for(let i=1; i<partList.length; i++){
            if(lastPart == partList[i]){
                count++;
            } else if(count == 1) {
                press += lastPart;
                count = 1
            } else {
                press += (""+count+lastPart);
                count = 1
            }
            lastPart = partList[i];
        }
        
        if(count == 1) {
            press += lastPart;
            count = 1
        } else {
            press += (""+count+lastPart);
            count = 1
        }
        caseLen.push(press.length)
    }
    
    
 
    return Math.min(...caseLen);
}