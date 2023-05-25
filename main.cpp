#include <iostream>

#include "raylib.h"

const int width = 400;
const int height = 400;
const int gridSize = width / 8;

int main(){
    InitWindow(width, height, "Hello World");
    SetTargetFPS(60);

    while (!WindowShouldClose()) {
        BeginDrawing();
            ClearBackground(RAYWHITE);

            // Draw Simple Grid
            for (int i = 0; i < 8; i ++){
                DrawLine(i * gridSize, 0, i * gridSize, height, BLACK);
            }
            for (int i = 0; i < 8; i ++){
                DrawLine(0, i * gridSize, width, i * gridSize, BLACK);
            }

        EndDrawing();
    }


    return 0;
}
