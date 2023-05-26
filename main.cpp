#include <bits/types/clock_t.h>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <map>

#include "raylib.h"

const int width = 400;
const int height = 400;
const int gridSize = 8;
const int cellSize = width / gridSize;

int grid[gridSize][gridSize][4]; // N S E W

int direction_map[4][2] = {
    {0, 1},
    {0, -1},
    {1, 0},
    {-1, 0},
};

void setup(){
    // Setup Random numbers
    srand(time(NULL));

    // Make a grid with walls on wall sides
    for(int i = 0; i < gridSize; i++){
        for(int j = 0; j < gridSize; j++){
            for(int k = 0; k < 4; k++){
                //if(rand() % 100 < 50)
                    grid[i][j][k] = 1;
            }
        }
    }
}

void carve(int x, int y, int grid[gridSize][gridSize][4]){
    int *walls = grid[x][y];

    int direction = rand() % 4;

    walls = grid[x + direction_map[direction][0]][y + direction_map[direction][1]];

}

int main(){
    InitWindow(width, height, "Hello World");
    SetTargetFPS(60);

    setup();

    while (!WindowShouldClose()) {
        BeginDrawing();
            ClearBackground(RAYWHITE);
            
            carve(0, 0, grid);

            // Draw
            for(int i = 0; i < gridSize; i++){
                for(int j = 0; j < gridSize; j++){
                    int *walls = grid[i][j];
                    if(walls[0] == 1) DrawLine(i * cellSize, j * cellSize, (i+1)*cellSize, j*cellSize, BLACK); // N
                    if(walls[1] == 1) DrawLine(i * cellSize, (j+1) * cellSize, (i+1)*cellSize, (j+1)*cellSize, BLACK); // S
                    if(walls[2] == 1) DrawLine((i+1) * cellSize, j * cellSize, (i+1)*cellSize, (j+1)*cellSize, BLACK); // E
                    if(walls[3] == 1) DrawLine(i * cellSize, j * cellSize, i*cellSize, (j+1)*cellSize, BLACK); // W
                }
            }

        EndDrawing();
    }

    return 0;
}