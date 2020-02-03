//+------------------------------------------------------------------+
//|                                                 Modify SL TP.mq4 |
//|                                 Copyright © 2020, FX Masterminds |
//|                                   https://lennykioko.github.io/" |
//+------------------------------------------------------------------+
#property copyright "Copyright � 2020, FX Masterminds."
#property link      "https://lennykioko.github.io/"

//version 1.0

//show input parameter
#property show_inputs


extern double sl = 0;
extern double tp = 0;
extern string comment = "";

//+------------------------------------------------------------------+
//| script program start function                                    |
//+------------------------------------------------------------------+

int start()
  {
//----
      int ordertotal = OrdersTotal();
      for (int i=0; i<ordertotal; i++)
      {
         int order = OrderSelect(i, SELECT_BY_POS,MODE_TRADES);
         if (OrderSymbol() == Symbol())
            if (OrderComment() == comment)
            {
               OrderModify(OrderTicket(), OrderOpenPrice(), sl, tp, 0);
            }
       }
//----
   return(0);
  }
//+------------------------------------------------------------------+
