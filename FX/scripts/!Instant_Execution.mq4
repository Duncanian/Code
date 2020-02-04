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
extern double  totalLot = 0.01;

enum e_type{
 pips=1,
 price=2,
};

input e_type  type = pips;

extern double sl = 0;
extern double tp = 0;


double lot = totalLot / numOfOrders;


double Poin;
//+------------------------------------------------------------------+
//| Custom initialization function                                   |
//+------------------------------------------------------------------+
int init() {

   if (Point == 0.00001) Poin = 0.0001;
   if (Point == 0.01) Poin = 0.1;
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
   Execute();
   if (type == 1) {
      ModifyPips();
   }
   if (type == 2) {
      ModifyPrice();
   }
   return(0);
}

int Execute() {
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

int ModifyPips() {
//----
   int ordertotal = OrdersTotal();
   for (int i=0; i<ordertotal; i++)
   {
      int order = OrderSelect(i, SELECT_BY_POS, MODE_TRADES);
      if (OrderSymbol() == Symbol())
         if (OrderComment() == comment && (OrderType()==OP_BUY || OrderType()==OP_BUYSTOP))
         {
            int ticket = OrderModify(OrderTicket(), OrderOpenPrice(), OrderOpenPrice()-sl*Poin, OrderOpenPrice()+tp*Poin, 0);
         }

         if (OrderComment() == comment && (OrderType()==OP_SELL || OrderType()==OP_SELLSTOP))
         {
            int ticket2 = OrderModify(OrderTicket(), OrderOpenPrice(), OrderOpenPrice()+sl*Poin, OrderOpenPrice()-tp*Poin, 0);
         }
      }
//----
return(0);
}


int ModifyPrice() {
//----
   int ordertotal = OrdersTotal();
   for (int i=0; i<ordertotal; i++)
   {
      int order = OrderSelect(i, SELECT_BY_POS, MODE_TRADES);
      if (OrderSymbol() == Symbol())
         if (OrderComment() == comment)
         {
            int ticket3 = OrderModify(OrderTicket(), OrderOpenPrice(), sl, tp, 0);
         }
      }
//----
return(0);
}
