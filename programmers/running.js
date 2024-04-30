// 틀린 문제풀이 - test 3개 런타임 초과
function solution(players, callings) {
    for(var i = 0; i < callings.length; i++) {
        x = players.indexOf(callings[i]);
        [players[x], players[x - 1]] = [players[x - 1], players[x]];
    }
    return players;
}