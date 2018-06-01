from pelix.ipopo.decorators import ComponentFactory, Provides, Instantiate
@ComponentFactory("helloimpl-provider-factory")
@Provides("org.eclipse.ecf.examples.hello.IHello")
@Instantiate("helloimpl-provider-auto", { "service.intents": ['osgi.basic', 'osgi.async'], 'osgi.basic.timeout':30000})
class HelloImpl(object):

    def sayHello(self, name='Not given', message = 'nothing'):
        print("Python.sayHello called by: {0} with message: '{1}'".format(name,message))
        return "Python says: Howdy {0} that's a nice runtime you got there".format(name)
 
    