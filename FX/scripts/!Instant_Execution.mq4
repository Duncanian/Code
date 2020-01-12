//+------------------------------------------------------------------+
//|                                             Instant_Execution.mq4 |
//+------------------------------------------------------------------+
#property copyright "Copyright � 2020, Lenny M Kioko."
#property link      "https://lennykioko.github.io/"

//version 1.0

//show input parameter
#property show_inputs

#include <stderror.mqh>
#include <stdlib.mqh>

//external parameters to be provided
extern string orderType = "";
extern int numOfOrders = 5;
extern string comment = "";
extern double  totalLot = 2.00;
// extern double  TP = 10.0;  // Mute SL&TP
// extern double  SL = 10.0;  // Mute SL&TP

double lot = totalLot / numOfOrders;


double Poin;
//+------------------------------------------------------------------+
//| Custom initialization function                                   |
//+------------------------------------------------------------------+
int init() {

   if (Point == 0.00001) Poin = 0.0001;
   else {
      if (Point == 0.001) Poin = 0.01;
      else Poin = Point;
   }
   return(0);
}
//+------------------------------------------------------------------+
//                                                                   +
//+------------------------------------------------------------------+
int start() {
   RefreshRates();
   while( IsTradeContextBusy() ) { Sleep(100); }
//----
   while( numOfOrders > 0) {
      if (orderType == "b") {
         int ticket = OrderSend(Symbol(), OP_BUY, lot, Ask, 3, 0.000, 0.000, comment, 11, 0, CLR_NONE);
      }
      if (orderType == "s") {
         ticket = OrderSend(Symbol(), OP_SELL, lot, Ask, 3, 0.000, 0.000, comment, 22, 0, CLR_NONE);
      }
      numOfOrders-=1;
   }
   if (ticket != numOfOrders) {
      int error = GetLastError();
      Print("Error = ", ErrorDescription(error));
      return ticket - numOfOrders;
   }
//----
   OrderPrint();
   return(0);
}
