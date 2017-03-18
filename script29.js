// Fill the empty space with the minimum number of rectangles.
// (Rectangles should not overlap each other or walls.)
// The grid size is 1 meter, but the smallest wall/floor tile is 4 meters.
// If you can do better than one rectangle for every tile, let us know!
// We'll help you find a programming job (if you want one).
// Check the blue guide button at the top for more info.
// Press Contact below to report success if you want a job!
// Just include your multiplayer link in the contact email.
// Make sure to sign up on the home page to save your code.

var my_max = function(grid)
{
    var my_max = 0;
    if (grid.length === 0)
        return 999999;
    for(var x = 0; x < grid.length ; x++)
    {
        for(var y = 0; y < grid[0].length ; y++)
        {
            if (my_max < grid[y][x])
                my_max = grid[y][x];
        }
    }
    return my_max;
};

var next_cel = function(grid,x,y)
{
    if (y+1 >= grid.length)
    {
        if (x+1 >= grid[0].length)
            return [0,0];
        else
            return [x+1,0];
    } else
    {
        return [x,y+1];
    }
};

var expand = function(grid,x,y,way,taille)
{
    stop = false;
    if (way == 'b')
    {
        while(y+taille[1]<grid.length && !stop)
        {
            for (var xa = 0 ; xa < taille[0] ; xa++)
            {
                if (grid[y+taille[1]][x+xa] != -1)
                {
                    stop = true;
                    break;
                }
            }
            if (!stop)
                taille[1] += 1;
        }
        return taille[1];
    } else
    {
     while(x+taille[0] < grid[0].length && !stop)
     {
         for (var ya = 0 ; ya < taille[1] ; ya++)
         {
             if (grid[y+ya][x+taille[0]] != -1)
             {
                 stop = true;
                 break;
             }
         }
         if (!stop)
            taille[0]+=1;
     }
        return taille[0];
    }
    return taille;
};

var mark = function(grid,x,y,taille,nb_rect)
{
    //if (nb_rect == 6)
    //    this.say(nb_rect+"=>"+x+":"+y+">"+taille);
    //this.wait();
    var tileSize = 4;
    for (var xa = 0; xa < taille[0]; xa++)
    {
        for (var ya = 0 ; ya < taille[1] ; ya++)
        {
            grid[y+ya][x+xa] = nb_rect;
        }
    }
    return grid;
};

var draw = function(result)
{
    var tileSize = 4;
    for (var i = 0 ; i < result.length ; i++)
    {
        this.addRect((result[i][0] + result[i][2] / 2)*tileSize, (result[i][1] + result[i][3] / 2)*tileSize, result[i][2]*tileSize, result[i][3]*tileSize);
    }
};

var resoudre = function(grid,x,y,start,nb_rect)
{
    result = [];
    while(true)
    {
        if (grid[y][x] == -1)
        {
            taille = [1,1];
            taille[0] = expand.call(this,grid,x,y,'r',taille);
            taille[1] = expand.call(this,grid,x,y,'b',taille);
            nb_rect++;
            grid = mark.call(this,grid,x,y,taille,nb_rect);
            result[result.length] = [x,y,taille[0],taille[1]];
        }
        pos = next_cel(grid,x,y);
        x = pos[0];
        y = pos[1];
        if (x == start[0] && y == start[1])
        {
            return result;
        }
    }
};

/*var result;
var mygrid = [[-1,-1,0],[0,-1,-1],[0,-1,-1]];
var start = [0,0];
result = resoudre.call(this,mygrid,0,0,start,0);
*/

var grid = this.getNavGrid().grid;
var tileSize = 4;
var waittime = 0;

var testCase = function(table,x,y)
{
    return (table[y][x]!=1);
};



// Populate table
var populate = function()
{
    var table = [];
    var line = [];
    for(var y = 0; y + tileSize < grid.length; y += tileSize) 
    {
        line = [];
        for(var x = 0; x + tileSize < grid[0].length; x += tileSize)
        {
            //this.say(grid[0][16].length);
            //this.say(x/tileSize + "," + y/tileSize + ":"+grid[y][x].length);
            //this.wait();
            if (grid[y][x].length > 0)
            {
                line[x/tileSize] = 0; // occupied
            } else
                line[x/tileSize] = -1; // free
        }
        table[y/tileSize] = line;
    }
    return table;
};

var copy_grid = function(grid)
{
    var result = [];
    for (var i = 0 ; i < grid.length ; i++)
    {
        result[i] = [];
        for (var j = 0 ; j < grid[0].length ; j++)
        {
            result[i][j] = grid[i][j];
        }
    }
    return result;
};
table = populate();
var nb_rect = 9999;
var better = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40];
for (y = 0 ; y < table.length; y++)
{
	for( x = 0 ; x < table[0].length ; x++)
	{
        table1 = copy_grid(table);
        var start = [x,y];
		var result = resoudre.call(this,table1,x,y,start);
		if (better.length > result.length)
		{/*
            this.say(x+":"+y);
            this.wait();
            this.say(result.length);
            this.wait();
            this.say(result);
            this.wait();*/
            better = result;
            /*this.say("ok");
            this.wait();*/
		}
	}
	this.say(better.length);
    //this.wait();
}
draw.call(this,better);
//result = resoudre.call(this,table,0,0,start,0);

/*
for(var y = 0; y + tileSize < grid.length; y += tileSize) 
{
    for(var x = 0; x + tileSize < grid[0].length; x += tileSize)
    {
        if (!testCase(table,x,y))
        {
            x_size = tileSize;
            y_size = 0;
            for (ay = y; !testCase(table,x,ay); ay += tileSize)
            {
                table[ay][0] = 2;
                y_size += tileSize;
            }
            this.say("Max y size :" + y_size);
            this.wait(waittime);
            for (ax = x+tileSize; !testCase(table,ax,y) ; ax += tileSize)
            {
                check = true;
                for (ay = y; ay - y <= y_size; ay += tileSize)
                {
                    if (testCase(table,ax,ay)) {
                        check = false;
                        break;
                    }
                }
                if (true)
                {
                    for (ay = y; ay - y <= y_size; ay += tileSize)
                    {
                        table[ay][ax] = 2;
                    }
                    x_size += tileSize;
                } else
                    break;
            }
            this.say("Max size :" + x_size + ":" + y_size);
            this.addRect(x + x_size / 2, y + y_size / 2, x_size, y_size);
            this.wait(waittime);
            this.wait();  // Hover over the timeline to help debug!
        }
    }
}*/

