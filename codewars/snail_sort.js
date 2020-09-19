function snail(m) {

    if (m.length <= 1) { return m[0]; }
    
    var max = { x: m.length - 1, y: m.length - 1 };
    var min = { x: 0, y: 0 };
    var current = { x: 0, y: 0 };
    var direction = { x: 1, y: 0 };
    var output = [];
    var resultSize = m.length * m.length;
    
    while (output.length != resultSize) {
    
        output.push(m[current.y][current.x]);
    
        current.x += direction.x;
        current.y += direction.y;
    
        if (current.x > max.x) { 
    
            direction.x = 0; direction.y = 1; min.y += 1; current.x = max.x; current.y += 1;
    
        } else if (current.x < min.x) { 
    
            direction.x = 0; direction.y = -1; max.y -= 1; current.x = min.x; current.y -= 1;
    
        } else if (current.y > max.y) { 
    
            direction.x = -1; direction.y = 0; max.x -= 1; current.y = max.y; current.x -= 1;
    
        } else if (current.y < min.y) { 
    
            direction.x = 1; direction.y = 0; min.x += 1; current.y = min.y; current.x += 1;
        }
    }
    
    return output;
    }