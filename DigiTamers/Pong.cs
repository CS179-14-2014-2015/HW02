﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Pong
{
    public partial class gameArea : Form
    {
        PictureBox picBoxPlayerOne, picBoxPlayerTwo, picBoxBall;
        Label playerOneScore_label, playerTwoScore_label;
        Timer gameTime;
        DialogResult gameResult;

        const int SCREEN_WIDTH = 800;
        const int SCREEN_HEIGHT = 600;

        Size sizePlayer = new Size(25, 100);
        Size sizePlayerTwo = new Size(25, 100);
        Size sizeBall = new Size(20, 20);

        int ballSpeedX = 3;
        int ballSpeedY = 3;
        int gameTimeInterval = 1;
        int playerOneScore = 0;
        int playerTwoScore = 0;

        private enum Direction { None, Up, Down };
        private Direction playerOneCurrentDir = Direction.None;
        private Direction currentDir = Direction.None;


        public gameArea()
        {
            InitializeComponent();

            
            KeyDown += new KeyEventHandler(Form_Keydown);
            KeyUp += new KeyEventHandler(playerTwo_Keyup);

            picBoxPlayerOne = new PictureBox();//
            picBoxPlayerTwo = new PictureBox();//Initializes the PictureBoxes
            picBoxBall = new PictureBox();//

            playerOneScore_label = new Label(); //Initializes labels for the scores
            playerTwoScore_label = new Label();

            gameTime = new Timer();//Initializes the Timer

            gameTime.Enabled = true;//Enables the Timer
            gameTime.Interval = gameTimeInterval;//Set the timer's interval

            gameTime.Tick += new EventHandler(gameTime_Tick);//Creates the Timer's Tick event

            this.Width = SCREEN_WIDTH;//sets the Form's Width
            this.Height = SCREEN_HEIGHT;//sets the Form's Height
            this.StartPosition = FormStartPosition.CenterScreen;//opens the form in center of the screen


            picBoxPlayerOne.Size = sizePlayer;//sets the size of the picturebox
            picBoxPlayerOne.Location = new Point(picBoxPlayerOne.Width / 2, ClientSize.Height / 2 - picBoxPlayerOne.Height / 2);//sets it's location (centered)
            picBoxPlayerOne.BackColor = Color.Blue;//fills the picturebox with a color
            this.Controls.Add(picBoxPlayerOne);//adds the picture box to the form

            picBoxPlayerTwo.Size = sizePlayerTwo;
            picBoxPlayerTwo.Location = new Point(ClientSize.Width - (picBoxPlayerTwo.Width + picBoxPlayerTwo.Width / 2), ClientSize.Height / 2 - picBoxPlayerOne.Height / 2);
            picBoxPlayerTwo.BackColor = Color.Red;
            this.Controls.Add(picBoxPlayerTwo);

            picBoxBall.Size = sizeBall;
            picBoxBall.Location = new Point(ClientSize.Width / 2 - picBoxBall.Width / 2, ClientSize.Height / 2 - picBoxBall.Height / 2);
            picBoxBall.BackColor = Color.Green;
            this.Controls.Add(picBoxBall);

            playerTwoScore_label.Text = playerTwoScore.ToString();
            playerTwoScore_label.Location = new Point(730, 540 );
            this.Controls.Add(playerTwoScore_label);

            playerOneScore_label.Text = playerOneScore.ToString();
            playerOneScore_label.Location = new Point(40, 540);
            this.Controls.Add(playerOneScore_label);
        }

        void gameTime_Tick(object sender, EventArgs e)
        {
            picBoxBall.Location = new Point(picBoxBall.Location.X + ballSpeedX, picBoxBall.Location.Y + ballSpeedY);
            gameAreaCollisions();//Checks for collisions with the form's border
            padlleCollision();//Checks for collisions with the padlles
            playerMovement();//Updates the player's position
            playerTwoMovement();//Updates the second player's position
        }

        private void gameAreaCollisions()
        {
            if (picBoxBall.Location.Y > ClientSize.Height - picBoxBall.Height || picBoxBall.Location.Y < 0)
            {
                ballSpeedY = -ballSpeedY;
            }
            else if (picBoxBall.Location.X > ClientSize.Width) // Scoring for Player One
            {
                playerOneScore++;
                playerOneScore_label.Text = playerOneScore.ToString();
                if (playerOneScore == 3)
                {
                    gameTime.Stop();
                    gameResult = MessageBox.Show("PLAYER ONE WINS! YEY!", "", MessageBoxButtons.OK);
                    if (gameResult == DialogResult.OK)
                    {
                        gameTime.Start();
                        resetBall();
                        playerOneScore = 0;
                        playerOneScore_label.Text = playerOneScore.ToString();
                    }
                }
                else
                { resetBall(); }
            }
            else if (picBoxBall.Location.X < 0) // Scoring for Player Two
            {
                playerTwoScore++;
                playerTwoScore_label.Text = playerTwoScore.ToString();
                if(playerTwoScore == 10)
                {
                    gameTime.Stop();
                    gameResult = MessageBox.Show("PLAYER TWO WINS! YEY!", "", MessageBoxButtons.OK);
                    if (gameResult == DialogResult.OK)
                    {
                        gameTime.Start();
                        resetBall();
                        playerTwoScore = 0;
                        playerTwoScore_label.Text = playerTwoScore.ToString();
                    }
                }
                else
                { resetBall();}
            }
        }

        private void resetBall()
        {
            picBoxBall.Location = new Point(ClientSize.Width / 2 - picBoxBall.Width / 2, ClientSize.Height / 2 - picBoxBall.Height / 2);
        }

        private void playerMovement() //Function for Player One Movement
        {
            int vel = 5;
            switch (playerOneCurrentDir)
            {
                case Direction.Up: picBoxPlayerOne.Top -= Math.Min(vel, picBoxPlayerOne.Top); break;
                case Direction.Down: picBoxPlayerOne.Top += Math.Min(vel, this.ClientSize.Height - picBoxPlayerOne.Bottom); break;
            }
        }

        private void playerTwoMovement() //Function for Player Two Movement
        {
            int vel = 5;
            switch (currentDir)
            {
                case Direction.Up: picBoxPlayerTwo.Top -= Math.Min(vel, picBoxPlayerTwo.Top); break;
                case Direction.Down: picBoxPlayerTwo.Top += Math.Min(vel, this.ClientSize.Height - picBoxPlayerTwo.Bottom); break;
            }
        }

        private void padlleCollision()
        {
            if (picBoxBall.Bounds.IntersectsWith(picBoxPlayerTwo.Bounds))
            {
                ballSpeedX = -ballSpeedX;
            }

            if (picBoxBall.Bounds.IntersectsWith(picBoxPlayerOne.Bounds))
            {
                ballSpeedX = -ballSpeedX;
            }
        }
        

        private void Form_Keydown(object sender, KeyEventArgs e) 
        {
            switch (e.KeyData)
            {
                case Keys.Up: currentDir = Direction.Up; break; // Press Up arrow key to make the paddle go up
                case Keys.Down: currentDir = Direction.Down; break; //Press Down arrow key to make the paddle go down
                case Keys.Escape: this.Close(); break; //Press Esc to exit the program
                case Keys.A: playerOneCurrentDir = Direction.Up; break; // Press A to make left paddle go up
                case Keys.S: playerOneCurrentDir = Direction.Down; break; //Press S to make left paddle go down
            }
                
        }

        private void playerTwo_Keyup(object sender, KeyEventArgs e) //Function to stop Player Two's paddle from moving
        {
            switch (e.KeyData)
            {
                case Keys.Up: if (currentDir == Direction.Up) currentDir = Direction.None; break;
                case Keys.Down: if (currentDir == Direction.Down) currentDir = Direction.None; break;
                case Keys.A: if (playerOneCurrentDir == Direction.Up) playerOneCurrentDir = Direction.None; break;
                case Keys.S: if (playerOneCurrentDir == Direction.Down) playerOneCurrentDir = Direction.None; break;
            }
        }
    }
}
