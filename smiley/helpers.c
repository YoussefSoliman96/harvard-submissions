#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int row = 0; row < width; row++)
    {
        for(int column = 0; column < height; column++)
        {
            if (image[height][width].rgbtBlue == 0 && image[height][width].rgbtGreen == 0 && image[height][width].rgbtRed == 0)
            {
                image[height][width].rgbtBlue = 255;
            }
        }
    }
}
