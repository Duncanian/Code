//+------------------------------------------------------------------+
//|                                             Buy_Contest_5_OP.mq4 |
//+------------------------------------------------------------------+
#property copyright "Copyright � 2010, eninefx."
#property link      "http://www.kaskus.us/showthread.php?t=3967467&page=350"

//versi 2.0 - 25-mei-2010

//munculkan parameter input
#property show_inputs

#include <stderror.mqh>
#include <stdlib.mqh>

//parameternya ini, input-nya ini
extern int numOfOrders = 4;
extern double orderPrice = 0.00;
extern string comment = "";
extern double  totalLot = 3.00;
// extern double  TP              = 10.0;  // Mute SL&TP
// extern double  SL              = 10.0;  // Mute SL&TP

double Lot = totalLot/numOfOrders;

double Poin;
//+------------------------------------------------------------------+
//| Custom initialization function                                   |
//+------------------------------------------------------------------+
int init(){

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
int start()
  {
   RefreshRates();
   while( IsTradeContextBusy() ) { Sleep(100); }
//----
   while( numOfOrders > 0) {
       int ticket = OrderSend(Symbol(),OP_BUYSTOP,Lot,orderPrice,3,0.000,0.000,comment,55,0,CLR_NONE);
       if(ticket<1)
       {
           int error=GetLastError();
           Print("Error = ",ErrorDescription(error));
           return;
        }
        numOfOrders-=1;
   }
//----
   OrderPrint();
   return(0);
  }

// ticket = OrderSend(  Sym,                    // Symbol
//                               OperationType,          // Operation type
//                               FixedLot,               // Lot size
//                               OrderPrice,             // Latest price for buy
//                               10,                     // Slippage
//                               SLPrice,                // Stop loss
//                               TPPrice,                // Take profit
//                               "Lucky",                // Comment
//                               MagicNumber,            // Magic number
//                               0,                      // Expiration
//                               clrNONE );              // Arrow color
